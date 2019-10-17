<template>
    <div>
        <div class="note" :style="note"></div>
        <el-card shadow="always" class="resCard">
            <h2 class="title">Register!</h2>
            <hr>
            <div class="registerForm">
                <span ><strong>Register：</strong></span><br>
                <el-input v-model="loginname" placeholder="Loginname" class="resinput" clearable></el-input>
                <el-input v-model="telnumber" placeholder="Tel Number" class="resinput" clearable></el-input>
                <el-input v-model="username" placeholder="Username" class="resinput" clearable></el-input>
                <el-input v-model="loginpwd" type="password" placeholder="Password" class="resinput"></el-input>
                <el-input v-model="reloginpwd" type="password" placeholder="Rewrite Password" class="resinput"></el-input>
                <el-button class="resbutton" type="text" @click="goLogin">Login</el-button>
                <el-button class="resbutton" type="primary" style="float:right;margin-right:20px;">Register</el-button>
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
            loginname:'',
            loginpwd:'',
            reloginpwd:'',
            username:'',
            telnumber:'',

        }
    },
    methods: {
        goLogin(){
            this.$router.push({path:'/user/login'});
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