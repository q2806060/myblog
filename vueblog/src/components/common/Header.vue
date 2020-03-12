<template>
    <el-header>
        <div class="container">
            <el-menu 
            :default-active="activeIndex" 
            class="menu-main" 
            mode="horizontal" 
            @select="handleSelect"
            text-color="black">
                <el-menu-item index="webMain" style="font-size:20px;margin-left:10px;font-weight:600">网站首页</el-menu-item>
                <el-submenu index="atcType" class="selectItem" style="margin-left:10px;">  
                    <template slot="title" v-if="articleTypeList">文章分类</template>
                    <el-menu-item 
                    v-for="articleType in articleTypeList" 
                    :index="articleType.id" 
                    :key="articleType.id">{{ articleType.title }}</el-menu-item>
                </el-submenu>
                <el-menu-item index="timeAxis" class="selectItem">时间轴</el-menu-item>
                <el-menu-item index="pubBlog" class="selectItem">发表博客</el-menu-item>
                <el-menu-item index="register" class="islogin" v-if="islogin==false">注册</el-menu-item>
                <el-menu-item index="login" class="islogin" v-if="islogin==false">登录</el-menu-item> 
                <el-menu-item index="logout" class="islogin" v-if="islogin">退出</el-menu-item>
                <el-menu-item index="username" class="islogin" v-if="islogin"><span>欢迎：</span>{{ username }}</el-menu-item>
            </el-menu>
            <hr>
        </div>
    </el-header>
</template>

<script>
export default {
    data() {
        return {
            articleTypeList:[
                {"title":"python基础", "id":"1"},
                {"title":"django","id":"2"}
            ],
            activeIndex:'',
            islogin:true,
            username:'11111111',

        }
    },
    methods: {
        handleSelect(key){
            if(key == "timeAxis"){
                this.$router.push({path:"/timeAxis"});
            }else if(key == "webMain"){
                this.$router.push({path:"/"})
            }else if(key == "pubBlog"){
                
            }else if(key == "register"){
                this.$router.push({path:"/register"})
            }else if(key == "logout"){
                this._logout()
            }else if(key == "username"){
                
            }else if(key == "login"){
                this.$router.push({path:"login"})
            }else{
                
            }
        },
        _logout(){
            let that = this;
            let url = DocConfig.server + '/user/logout';
            that.axios.get(url)
                .then((response) => {
                    if(response.data.error_code == 0){
                        this.$router.push({path:"/"})
                    }
                }).catch((error) => {
                    console.log(error)
                })
        },
    },
}
</script>

<style scoped>
body{
    margin: 0;
}
.el-header{
    width: 100%;
    text-align: center;

}

.menu-main{
    background-color: rgba(255, 255, 255, 0);
}
hr{
    margin: 0;
}
.islogin{
    float: right;
}
</style>