<template>
    <div>
        <div class="note" :style="note"></div>
        <el-card shadow="always" class="loginCard">
            <h2 class="title">Login!</h2>
            <hr>
            <div class="loginForm">
                <span><strong>Login：</strong></span>
                <el-form ref="FormData" :model="FormData">
                    <el-form-item 
                        class="logininput"
                        prop="loginname"
                        :rules="{ required: true, message: 'Please input loginname', trigger: 'blur'}">
                        <el-input 
                            v-model="FormData.loginname" 
                            placeholder="Loginname" 
                            clearable
                            autocomplete="off">
                        </el-input>
                    </el-form-item>
                    <el-form-item 
                        class="logininput"
                        prop="loginpwd"
                        :rules="{ required: true, message: 'Please input password', trigger: 'blur'}">
                        <el-input 
                            v-model="FormData.loginpwd" 
                            type="password" 
                            placeholder="Password"  
                            show-password
                            autocomplete="off">
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button 
                            class="loginbutton" 
                            type="text" 
                            @click="goRegister">Register</el-button>
                        <el-button 
                            class="loginbutton" 
                            type="primary" 
                            style="float:right;margin-right:20px;" 
                            @click="goLogin('FormData')">Login</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
            note:{
                backgroundImage: "url(" + require("../../assets/zd01.jpg") + ")",
            },
            FormData:{
                loginname:'',
                loginpwd:'',
            },

        }
    },
    methods: {
        goRegister(){
            this.$router.push({path:'/user/register'})
        },
        goLogin(FormName){
            this.$refs[FormName].validate((valid) => {
                if(valid){
                    let that = this;
                    let url = DocConfig.server + "/user/login";
                    let params = new URLSearchParams();
                    params.append("loginname", that.FormData.loginname);
                    params.append("password", that.FormData.loginpwd);
                    that.axios.post(url, params)
                        .then(function(response){

                            if(response.data.error_code == 0){
                                that.$router.push({path:"/"})
                            }else{
                                alert(response.data.data.error_msg)
                            }
                        }).catch((error) => {
                            alert(error)
                        })
                }else{
                    alert("error login")
                }
            })
            
        },

    }
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
}
.loginCard{
    margin: 100px auto;
    height: 400px;
    width: 400px;
    border-radius: 10px;
    opacity: 1;
}
.title{
    text-align: center;
    margin-top: 0px;
}
.loginForm{
    margin-top: 50px;
    margin-left: 20px;
}
.logininput{
    margin-top: 10px;
}
.loginbutton{
    margin-top: 40px;
    width: 100px;
}
</style>