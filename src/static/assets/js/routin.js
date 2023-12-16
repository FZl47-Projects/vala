import {getAllRoutinwithuser} from "./api/routin.js"
const routin =await  getAllRoutinwithuser(localStorage.getItem("user"))
console.log(routin);
routin.forEach(item => {
    item.value = item.value.replace(/\n/g,"</br>")
    const note = 
    `<div class="rotin-item">
    ${item.value}
    </div>`
    document.querySelector("#routinnotif").innerHTML+=note
});