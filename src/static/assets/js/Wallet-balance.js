import { getUserLocal } from "./api/validateLoginUser.js";

await getUserLocal();


/*------------------------------Render Page--------------------------------- */

let btnHamburger = document.querySelectorAll(".inner-menu-mobile");
btnHamburger.forEach((item, index) => {
  item.addEventListener("click", () => {
 
    btnHamburger[index].classList.toggle("active");
   
  });
});


/*------------------show and close modal-adamtaeid ------------------- */


/* ------------------change img and content--------------------- */
let btns = document.querySelectorAll(".btn-change");
let contents = document.querySelectorAll(".content");

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

