import { getUserLocal } from "./api/validateLoginUser.js`";

await getUserLocal();


/* ------------------change img and content--------------------- */
let btns = document.querySelectorAll(".inner-custom-box");
let contents = document.querySelectorAll(".content-pakage");

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