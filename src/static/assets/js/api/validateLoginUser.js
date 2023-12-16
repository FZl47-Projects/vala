const getUserLocal = async() => {
    const user = window.localStorage.getItem("user");
    if(!user){
        window.location.replace("./sign-up.html")
    }else {
        return;
    }
}

export {getUserLocal}