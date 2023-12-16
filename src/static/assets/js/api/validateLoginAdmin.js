const validateLogin = async() => {
    const user = window.localStorage.getItem("user-admin");
    if(!user){
        window.localStorage.setItem("user-admin",1)
        // window.location.replace("http://185.255.89.163:8080/admin/sign-up-in.html")
    }else {
        return;
    }
}



export {validateLogin}