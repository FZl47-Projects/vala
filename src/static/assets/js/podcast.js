import { getUserLocal } from "./api/validateLoginUser.js";

await getUserLocal();
 /*------------------------------Render Page--------------------------------- */

//  let btnHamburger = document.querySelectorAll(".inner-content-post-two");
//  btnHamburger.forEach((item, index) => {
//    item.addEventListener("click", (e) => {
//     console.log(e.target.className);
//     if(e.target.className === "heart" || e.target.className === "comment")
//      btnHamburger[index].classList.toggle("active");
//    });
//  });


 /* ------------------change img and content--------------------- */
 let btns = document.querySelectorAll(".post-item");
 let contents = document.querySelectorAll(" .content-post");

 btns.forEach((item, index) => {
   item.addEventListener("click", () => {
     btns.forEach((item) => {
       item.classList.remove("active");
     });
     contents.forEach((item) => {
       item.classList.remove("active");
     });
     btns[index].classList.add("active");
     contents[index].classList.add("active");
   });
 });

/* ------------------change img and content--------------------- */
/*----------------------------(show , close , send) modal add-post --------------------------- */
const btnsShowModal = document.querySelectorAll(".icon-add");
const btnsCloseModal = document.querySelectorAll(".close-modal-adamtaeid");
const btnsSendModal = document.querySelectorAll(".btn-send-modal");
const valueModals = document.querySelectorAll(".input-modal");
const contentModals = document.querySelectorAll(".modal-add-post");

btnsShowModal.forEach((item, index) => {
  item.addEventListener("click", () => {
    contentModals[index].classList.add("active");
  });
});

btnsCloseModal.forEach((item, index) => {
  item.addEventListener("click", () => {
    contentModals[index].classList.remove("active");
  });
});

contentModals.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
      contentModals[index].classList.remove("active");
  });
});
/*----------------------------(show , close , send) modal add-post --------------------------- */
/* ------------------menu-desk-------------------- */
let btnss = document.querySelectorAll("#menuuuu");
let contentss = document.querySelector("#height-full-viewport-desk");
let close_btn = document.querySelector("#close");

//   btns.addEventListener("click", () => {
//       contents.classList.add("viewport");
//     });
btnss.forEach((item) => {
  item.addEventListener("click", () => {
    contentss.classList.add("viewport");
  });
});

close_btn.addEventListener("click", () => {
  contentss.classList.remove("viewport");
});

/* ------------------menu-desk-------------------- */
/* ------------------menu-mobile-------------------- */
let btnss_m = document.querySelectorAll("#menuuuu-b");
let contentss_m = document.querySelector("#height-full-viewport-mobile");
let close_btn_m = document.querySelector("#close-2");


//   btns.addEventListener("click", () => {
//       contents.classList.add("viewport");
//     });
btnss_m.forEach((item) => {
  item.addEventListener("click", () => {
    contentss_m.classList.add("viewport");
  });
});
close_btn_m.addEventListener("click", () => {
  contentss_m.classList.remove("viewport");
});
/* ------------------menu-mobile-------------------- */

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

/*----------------------------(show , close , send) modal rotin --------------------------- */
/*----------------------------(show , close , send) modal add-post --------------------------- */
const btnsShowModalazmayesh = document.querySelectorAll("#azmayesh-raygan");
const btnsCloseModalazmayesh = document.querySelector("#close-modal-azmayesh");
const contentModalsazmayesh = document.querySelector(".modal-azmayesh-raygan");

btnsShowModalazmayesh.forEach(item=>{
  item.addEventListener('click',()=>{
    contentModalsazmayesh.classList.add("active");
  })
})

   btnsCloseModalazmayesh.addEventListener("click", () => {
    contentModalsazmayesh.classList.remove("active");
  });


  contentModalsazmayesh.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
    contentModalsazmayesh.classList.remove("active");
  });

/*----------------------------(show , close , send) modal add-post --------------------------- */