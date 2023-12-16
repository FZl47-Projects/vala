
import { getUserLocal } from "./api/validateLoginUser.js";

await getUserLocal();
/*----------------------------(show , close , send) modal rotin --------------------------- */
const btnsShowModalrotin = document.querySelectorAll("#icon-add-rotin");
const btnsCloseModalrotin = document.querySelector("#close-modal-rotin");
const contentModalsrotin = document.querySelector(".modal-rotin");

btnsShowModalrotin.forEach(item=>{
  item.addEventListener('click',()=>{
    contentModalsrotin.classList.add("active");
  })
})

  btnsCloseModalrotin.addEventListener("click", () => {
    contentModalsrotin.classList.remove("active");
  });


  contentModalsrotin.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
      contentModalsrotin.classList.remove("active");
  });

  /*----------------------------(show , close , send) modal answer --------------------------- */
const btnsShowModal = document.querySelectorAll("#btn-modal-1");
const btnsCloseModal = document.querySelector(".close-modal-adamtaeid");
// const btnsSendModal = document.querySelectorAll(".btn-send-modal");
// const valueModals = document.querySelectorAll(".input-modal");
const contentModals = document.querySelector(".modal-ticket");

btnsShowModal.forEach(item=>{
    item.addEventListener('click',()=>{
        contentModals.classList.add("active");
    })
  })


    btnsCloseModal.addEventListener("click", () => {
    contentModals.classList.remove("active");
  });


contentModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
    contentModals.classList.remove("active");
  });

/*----------------------------(show , close , send) modal modal answer --------------------------- */
/*----------------------------(show , close , send) modal answer --------------------------- */
const btnsmoshavereh = document.querySelectorAll("#btn-moshavereh");
const btnsClosemoshavereh = document.querySelector(".close-modal-adamtaeiid");
// const btnsSendModal = document.querySelectorAll(".btn-send-modal");
// const valueModals = document.querySelectorAll(".input-modal");
const contentModalsmoshavereh = document.querySelector(".modal-moshaveraeh");

btnsmoshavereh.forEach(item=>{
    item.addEventListener('click',()=>{
        contentModalsmoshavereh.classList.add("active");
    })
  })


  btnsClosemoshavereh.addEventListener("click", () => {
    contentModalsmoshavereh.classList.remove("active");
  });


  contentModalsmoshavereh.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
    contentModalsmoshavereh.classList.remove("active");
  });

/*----------------------------(show , close , send) modal modal answer --------------------------- */