
import { getAllUsers,updateUser } from "../api/user.js"
import {  phoneHandlerReverse,phoneHandler } from "../helper.js"
import { validateLogin } from "../api/validateLoginAdmin.js";
import { addUser } from "../api/signandlogin.js";
await validateLogin()
/*---------------- render page -------------------*/


const allUsers = await getAllUsers()
console.log(allUsers)

const renderpage =async() => {

    const container = document.querySelector("#container")

    allUsers.forEach((item , index) => {
        if(item.pin==true){
        const pin=`   <div class="col-12 col-md-3 p-2" id="item">
        <div class="cartex-item">
       
            <div class="main-content">
                <div class="right-cartex-item col-10">
                    <div class="name title" data-national="${item.nationalcode}">${item.name}</div>
                    <div class="phonne-number">${phoneHandlerReverse(item.phone_number)}</div>
                </div>

                <div class="left-cartex-item col-2">
                <div onclick = "pin(${item.id},false)" class ="icon-left" style="padding:5px; cursor: pointer"> <img src="/assets/images/pin.png" alt=""></div>
                  
                </div>

            </div>
            <a href="./cartex.html?user-id=${item.id}" class="show-information d-block text-center">مشاهده اطلاعات</a>
            
        </div>
    </div>`
    document.querySelector("#pin").innerHTML+=pin
        }
        const note = `
        <div class="col-12 col-md-3 p-2" id="item">
        <div class="cartex-item">
       
            <div class="main-content">
                <div class="right-cartex-item col-10">
               
                    <div class="name title" data-national="${item.nationalcode}">${item.name}</div>
                    <div class="phonne-number">${phoneHandlerReverse(item.phone_number)}</div>
                </div>
                <div class="left-cartex-item col-2">
                <div onclick = "pin(${item.id},true)"  class ="icon-left" style="padding:5px; cursor: pointer"> <img src="/assets/images/pin.png" alt=""></div>
                  
                </div>

            </div>
            <a href="./cartex.html?user-id=${item.id}" class="show-information d-block text-center">مشاهده اطلاعات</a>
            
        </div>
    </div>
        
        `
        container.innerHTML += note 

    });


}


await renderpage()
/*--------------- render page --------------------*/
// search
const inputSearchF = document.querySelector(".input-header");
const allUserF = document.querySelectorAll(
  "#item"
);

inputSearchF.addEventListener("input", () => {
    console.log("hellp");
  let search = inputSearchF.value.toLowerCase();

  for (let i of allUserF) {
    let item = i.querySelector(".title").innerHTML.toLowerCase();
    let national = i.querySelector(".title").getAttribute("data-national");
    if (item.indexOf(search) == -1 && national.indexOf(search) == -1) {
      i.classList.add("d-none");
    } else {
      i.classList.remove("d-none");
    }
  }
});
// end


const btnAddUser = document.querySelector(".add-user");
const btnCloseModalAddUser = document.querySelector(".close-modal-add-user");
const ModalAddUser = document.querySelector(".modal-add-user");
const OverlyModalAddUser = document.querySelector(".modal-add-user .inner-modal");


btnAddUser.addEventListener("click", () => {
  ModalAddUser.classList.add("active");
});

btnCloseModalAddUser.addEventListener("click", () => {
  ModalAddUser.classList.remove("active");
});
OverlyModalAddUser.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal")
  ModalAddUser.classList.remove("active");
});
const submitBtn = document.querySelector("#add-post")
submitBtn.addEventListener('click',async()=>{
  const name = document.querySelector("#nameUser").value
  const nationalCode = document.querySelector("#nationalCodeUser").value
  const phone_number = document.querySelector("#phoneNumberUser").value
  const data ={
    name,
    phone_number:phoneHandler(phone_number) ,
    age:1,
    weight:1,
    height:1,
    nationalcode:nationalCode,
    password :123,
    birthday:"2020-1-1",
    wallet:0,
    pin :true

  }
  console.log(data);
  var requestOptions = {
    headers: {
      'Accept': 'application/json, text/plain',
      'Content-Type': 'application/json;charset=UTF-8'
  },
    method: "POST",
    body: JSON.stringify(data),
    redirect: "follow",
  };

 console.log( await addUser(requestOptions))
})

window.pin = async(id,status)=>{
  await updateUser(id,{"pin":status})
  location.reload()
}