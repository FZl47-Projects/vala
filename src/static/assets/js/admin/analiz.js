import { getAllanalyze } from "../api/analyze.js";
import {addRoutin} from "../api/routin.js"
const getAllanalyze2 = await getAllanalyze();

const renderPage = async() =>{
   console.log(getAllanalyze2);
   getAllanalyze2.forEach(item=>{
       console.log(item);
    const container = document.querySelector("#container")
    const Modalanalyz = document.querySelector("#modal-analiz")
    const note = `<div class="list-analiz">
    <div class="col-2" style="text-align:center ;">
        <div class="list-analiz-item">
            ${item.user.name}
        </div>
        
    </div>
    <div class="col-3" style="text-align:center ;">
        <div class="list-analiz-item">
        ${item.user.phone_number}
        </div>
        
    </div>
    <div class="col-3" style="text-align:center ;">
        <div class="list-analiz-item">
        ${item.user.nationalcode}
        </div>
        
    </div>
    <div class="col-2 " style="text-align:center ;">
        <div class="list-analiz-item  nnn">
            نمایش روتین 
        </div>
       
    </div>
    <div class="col-2" style="text-align:center ;">
        <div class="list-analiz-item" id="tarif-rotinbtn">تعریف  روتین</div>
    </div>
</div>`;


const  modalAnaliz = `
<div class="content-modal modal-analiz">
        <div class="inner-modal">
            <div class="analiz-box">
                <div class="close-modal-analiz">
                    <img src="../assets/images/icon-valla/close.png" alt="">
                </div>
                <div class="row">
               <div class="col-4 img-analiz"><img src="${item.image1}"></div>
               <div class="col-4 img-analiz"><img src="${item.image2}"></div>
               <div class="col-4 img-analiz"><img src="${item.image3}"></div>
                </div>
               
            </div>
      </div>
    </div>

`;
const modalRoutin = `                <div class="content-modal  modal-tarif-rotin">
<div class="inner-modal">
  <form class="px-4 pt-2">
    <div class="py-2">
      <div class="title">
        <div id="close-modal-tarif-rotin" style="cursor:pointer ;"><img
            src="../assets/images/icon-valla/close.png" alt=""></div>
        <div style="font-size: 1.5em;">تعریف روتین </div>
      </div>
      
      </label>
      <textarea
        name="modal"
        class="input-modal"
        id="des-routin"
        cols="30"
        rows="7"
        placeholder="توضیخات خود را بنویسید"></textarea>
    </div>
    <div class="btn-modal" >
      <div class="btn-sabt-post" id="btn-add-routin" onclick="addroutin(${item.user.id})">
        ثبت
      </div>
    </div>
  </div>
</form>
</div>`;
  console.log(item.image1);
    container.innerHTML += note
    Modalanalyz.innerHTML += modalAnaliz
    Modalanalyz.innerHTML += modalRoutin
   })
  }
  
  await renderPage()




























const display_analiz = document.querySelectorAll(".nnn");
const modal_analiz_face = document.querySelectorAll(".modal-analiz");
const close_analiz_face = document.querySelectorAll(".close-modal-analiz")

display_analiz.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_analiz_face[index].classList.add("active");
    });
});
close_analiz_face.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_analiz_face[index].classList.remove("active");
    });
  });

const tarif_rotin_btn = document.querySelectorAll("#tarif-rotinbtn");
const modal_tarif_rotin = document.querySelectorAll(".modal-tarif-rotin");
const close_tarif_rotin = document.querySelectorAll("#close-modal-tarif-rotin")

tarif_rotin_btn.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_tarif_rotin[index].classList.add("active");
    });
});
close_tarif_rotin.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_tarif_rotin[index].classList.remove("active");
    });
  });
  close_tarif_rotin.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_tarif_rotin[index].classList.remove("active");
    });
  });
  modal_tarif_rotin.forEach((item, index) => {
    item.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal")
        modal_tarif_rotin[index].classList.remove("active");
    });
  });
  
// add routin 

window.addroutin=async (id)=>{
    const data={
        "name":"empty",
        "types":"food",
        "value":document.querySelector("#des-routin").value,
        "user":id,
        "isActive":true
    }
    console.log(await addRoutin(data));
    
}