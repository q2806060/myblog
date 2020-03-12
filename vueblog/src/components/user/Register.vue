<template>
    <div>
        <div class="note" :style="note"></div>
        <el-card shadow="always" class="resCard">
            <h2 class="title">Register!</h2>
            <hr>
            <div class="registerForm">
                <span ><strong>Register：</strong></span><br>
                <el-form :model="registerForm" ref="registerForm">
                    <el-form-item 
                        class="resinput" 
                        prop="loginname"
                        :rules="{ required: true, message: 'Please input loginname', trigger: 'blur'}"
                        @blur="checkName">
                        <el-input 
                            v-model="registerForm.loginname" 
                            placeholder="Loginname"  
                            clearable></el-input>
                    </el-form-item>
                    <el-form-item 
                        class="resinput" 
                        prop="telnumber"
                        :rules="[{ required: true, message: 'Please input telnumber', trigger: 'blur'},
                                { type: 'number', message: 'Please input right telnumber'}]">   
                        <el-input 
                            v-model.number="registerForm.telnumber" 
                            placeholder="Tel Number"  
                            clearable></el-input>
                    </el-form-item>
                    <el-form-item 
                        class="resinput" 
                        prop="username"
                        :rules="{ required: true, message: 'Please input username', trigger: 'blur'}">    
                        <el-input 
                            v-model="registerForm.username" 
                            placeholder="Username"  
                            clearable></el-input>
                    </el-form-item>
                    <el-form-item 
                        class="resinput" 
                        prop="loginpwd"
                        :rules="{ required: true, message: 'Please input password', trigger: 'blur'}">    
                        <el-input 
                            v-model="registerForm.loginpwd" 
                            type="password" 
                            placeholder="Password" ></el-input>
                    </el-form-item>
                    <el-form-item 
                        class="resinput" 
                        prop="reloginpwd"
                        :rules="{ required: true, message: 'Please input password', trigger: 'blur'}">   
                        <el-input 
                            v-model="registerForm.reloginpwd" 
                            type="password" 
                            placeholder="Rewrite Password" ></el-input>
                    </el-form-item>
                    <el-form-item>    
                        <el-button class="resbutton" type="text" @click="goLogin">Login</el-button>
                        <el-button class="resbutton" type="primary" style="float:right;margin-right:20px;" @click="goRegister('registerForm')">Register</el-button>
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
                backgroundImage: "url(" + require("../../assets/bi05.jpg") + ")",
            },
            registerForm:{
                loginname:'',
                loginpwd:'',
                reloginpwd:'',
                username:'',
                telnumber:'',
            },
        }
    },
    methods: {
        goLogin(){
            this.$router.push({path:'/user/login'});
        },
        goRegister(FormName){
            this.$refs[FormName].validate((valid) => {
                if(valid && this.checkPwd()){
                    let that = this;
                    let url = DocConfig.server + '/user/register';
                    let params = new URLSearchParams();
                    params.append("loginname", that.registerForm.loginname);
                    params.append("loginpwd", that.registerForm.loginpwd);
                    params.append("username", that.registerForm.username);
                    params.append("telnumber", that.registerForm.telnumber);
                    that.axios.post(url, params)
                        .then((response) => {
                            if(response.data.error_code == 0){
                                alert(response.data.data.msg)
                                that.$router.push({path:"/"})
                            }else{
                                alert(response.data.data.error_msg)
                            }
                        }).catch((error) => {
                            alert(error)
                        })
                }else{
                    alert("error register")
                }
            })
        },
        checkPwd(){
            if(this.registerForm.loginpwd == this.registerForm.reloginpwd){
                return true;
            }else{
                return false;
            }
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
    opacity: 0.8;
}
.resCard{
    margin: 100px auto;
    width: 450px;
    height: 600px;
    border-radius: 10px;
}
.title{
    text-align: center;
    margin-top: 0;
}
.resinput{
    margin-top: 10px;
}
.registerForm{
    margin-top: 50px;
    margin-left: 20px;   
}
.resbutton{
    margin-top: 40px;
    width: 100px;
}

</style>