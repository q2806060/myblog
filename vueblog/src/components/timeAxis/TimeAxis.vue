<template>
    <div>
        <div class="note" :style="note"></div>
        <el-container direction="vertical">
            <Header></Header>
            <el-main class="">
                <div class="timeMain">
                    <div class="sortRadio">
                        <div style="margin-left:50px;font-size:24px;display:inline-block;margin-top:40px;">排序：</div>
                        <el-radio-group v-model="reverse">
                            <el-radio :label="true">倒序</el-radio>
                            <el-radio :label="false">正序</el-radio>
                        </el-radio-group>
                        <div v-if="islogin" style="margin-left:530px;display:inline-block">
                            <el-button type="primary" @click="dialogTable = true" >
                                添加
                            </el-button>
                            <el-dialog title="增加时间轴" :visible.sync="dialogTable">
                                <el-form :model="timeForm">
                                    <el-form-item label="标题">
                                        <el-input v-model="timeForm.title" autocomplete="off"></el-input>
                                    </el-form-item>
                                    <el-form-item label="更新内容">
                                        <el-input v-model="timeForm.content" type="textarea" autocomplete="off"></el-input>
                                    </el-form-item>
                                    <el-form-item>
                                        <el-button type="primary" @click="addTimeaxis">
                                            提交
                                        </el-button>
                                    </el-form-item>
                                </el-form>
                            </el-dialog>
                        </div>
                    </div>
                    <el-timeline :reverse="reverse">
                        <el-timeline-item
                            v-for="(item, index) in items[0]"
                            :key="index"
                            :timestamp="item.fields.pubtime"
                            placement="top"
                            :style="{color:'black'}">
                            <el-collapse :model="item.fields">
                                <el-collapse-item :name="index">
                                    <template slot="title">
                                        <span  style="font-size:18px;font-weight:600;margin-left:20px;margin-right:20px">
                                            {{ item.fields.title }}
                                        </span>
                                    </template>
                                    <pre style="margin-left:20px;margin-right:20px;font-size:14px;font-weight:500">{{ item.fields.content }}</pre>
                                </el-collapse-item>
                            </el-collapse>
                        </el-timeline-item>
                    </el-timeline>
                </div>
            </el-main>
            
        </el-container>
    </div>
</template>

<script>
export default {
    data() {
        return {
            note:{
                backgroundImage:"url(" + require("../../assets/time.jpg") + ")",
            },
            reverse:true,
            items:[],
            islogin:true,
            timeForm:{
                title:'',
                content:'',
            },
            dialogTable:false,
            

        }
    },
    methods: {
        _getTimeaxis(){
            let that = this;
            let url = DocConfig.server + '/main/timeaxis';
            let items = [];
            that.axios.get(url)
                .then((response) => {
                    if(response.data.error_code == 0){
                        console.log(response.data);
                        // items = JSON.parse(response.data.data);
                        console.log(response.data.data[0].fields.title);
                        that.items.push(response.data.data);
                        console.log(that.items)
                        
                    }
                }).catch((error) => {
                    console.log(error)
                })
        },
        addTimeaxis(){
            let that = this;
            let url = DocConfig.server + '/main/timeaxis';
            let params = new URLSearchParams();
            params.append("title", that.timeForm.title);
            params.append("content", that.timeForm.content);
            that.axios.post(url, params)
                .then((response) => {
                    if(response.data.error_code == 0){
                        alert(response.data.data.msg);
                        that._getTimeaxis();
                    }else{
                        alert(response.data.data.error_msg);
                        that._getTimeaxis();
                    }
                }).catch((error) => {
                    alert("添加错误")
                    that._getTimeaxis();
                })
        }
    },
    mounted() {
        this._getTimeaxis();
    },
}
</script>

<style scoped>
.note{
    position: fixed;
    height: 100%;
    width: 100%;
    background: no-repeat center top;
    background-size: cover;
    z-index: -100;
    top: 0;
    left: 0;
    opacity:0.7;
}
.timeMain{
    width: 80%;
    margin: 0 auto;
}
.sortRadio{
    margin-bottom: 10px;
}
pre{
    white-space:pre-wrap; /* css3.0 */ 
    white-space:-moz-pre-wrap; /* Firefox */ 
    white-space:-pre-wrap; /* Opera 4-6 */ 
    white-space:-o-pre-wrap; /* Opera 7 */ 
    word-wrap:break-word; /* Internet Explorer 5.5+ */ 
}
</style>