import { getUserWithId } from "./api/user.js";

// await getUserLocal();

const userinfo = await getUserWithId(localStorage.getItem("user"));
const price = document.querySelector(".price").innerHTML =userinfo.wallet
const Percent = document.querySelectorAll("#Percent")


console.log(Percent);
const dataper=[
  {
    "name":"test1",
    "price":110
  },
  {
    "name":"test2",
    "price":120
  },
  {
    "name":"test3",
    "price":130
  },
  {
    "name":"test4",
    "price":140
  }
]
const award = document.querySelectorAll("#award")
Percent.forEach((item,index)=>{
  console.log(userinfo.wallet*100/dataper[index].price);
  item.value = userinfo.wallet*100/dataper[index].price
  award[index].innerHTML=dataper[index].price+"امتیاز"
})
let btnHamburger = document.querySelector(".menu-admins");

  
btnHamburger.addEventListener("click", (e) => {
  if (
    e.target.className === "price" ||
    e.target.className === "des" ||
    e.target.className === "Wallet-balance"
  ){
    
    btnHamburger.classList.toggle("active");
  }else{
    return;
  }
});
