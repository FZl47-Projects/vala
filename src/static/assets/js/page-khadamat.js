import { getAllManagers } from "./api/managers.js";
import { getPath } from "./helper.js";


const path = await getPath(window.location.search);

const managers = await getAllManagers();

/*--------------render page------------------*/
const renderPage = async () => {
  const filterManagers = managers.filter((item) => item.types === path);

  const container = document.querySelector("#container");

  filterManagers.forEach((item, index) => {
    const note = `<div class="col-12 p-2">
        <a href="./portfolio.html?${item.id}">
            <div class="item-user">
                <div class="col-3 col-md-2">
                    <div class="image-user">
                        <img
                            src="http://185.255.89.163:8000${item.image}"
                            alt="">
                    </div>
                </div>

                <div class="col-9 col-md-10 nnn">
                    <div class="name-user">
                        ${item.name}
                  </div>
                </div>
            </div>
        </a>

    </div>`;
    container.innerHTML += note;
  });
};

await renderPage();
/*--------------render page------------------*/
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




