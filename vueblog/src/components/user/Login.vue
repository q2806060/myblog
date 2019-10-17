<template>
    <div>
        <div class="note" :style="note"></div>
        <el-card shadow="always" class="loginCard">
            <h2 class="title">Login!</h2>
            <hr>
            <div class="loginForm">
                <span><strong>Login：</strong></span>
                <el-input v-model="loginname" placeholder="Loginname" class="logininput" clearable></el-input>
                <el-input v-model="loginpwd" type="password" placeholder="Password" class="logininput" show-password></el-input>
                <el-button class="loginbutton" type="text" @click="goRegister">Register</el-button>
                <el-button class="loginbutton" type="primary" style="float:right;margin-right:20px;" @click="goLogin">Login</el-button>
                <el-input type="hidden" id="csrfmiddlewaretoken" name="csrfmiddlewaretoken" value="csrf_token"></el-input>
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
            loginname:'',
            loginpwd:'',
            csrf_token:'',
        }
    },
    methods: {
        goRegister(){
            this.$router.push({path:'/user/register'})
        },
        goLogin(){
            let that = this;
            let url = DocConfig.server + "/get_data";
            let params = new URLSearchParams();
            params.append("content", that.loginname);
            params.append("csrfmiddlewaretoken", that.csrf_token);
            that.axios.get(url)
                .then(function(response){
                    console.log(response.Data)
                })
            // that.axios.post(url, params)
            //     .then(function(response){
            //         console.log(response);
            //     })
        }

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