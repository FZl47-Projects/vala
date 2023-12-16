import { getAllReserve } from "../api/reserve.js";

/*----------------------render Page---------------------*/
const allReserve = await getAllReserve();

const renderPage = async () => {

const container = document.querySelector("#container")    
    allReserve.forEach((item , index) => {
        console.log(item)
        const note =`<div class="col-12 col-md-6 p-1">
        <div class="item-ticket d-flex justify-content-between  flex-column">
            <div class="d-flex justify-content-between align-items-center">
                <div class="title d-flex justify-content-between align-items-center my-2">
                <span>رضا اخوندی</span>
              </div>
              <div class="des-1">
                     09338564893
              </div>
            </div>
            <div class="text-white d-flex justify-content-between align-items-center">
                <span>${item.description}</span>
                <div>
                    <span class="btn btn-success btn-sm mx-2">تایید شده</span>
                    <span class="btn btn-danger btn-sm"> حذف</span>
                </div>
            </div>
            
          </div>
    </div>`


    container.innerHTML+= note
    });
};

await renderPage();
/*---------------------render Page----------------------*/
/* ------------------change img and content--------------------- */
let btnss = document.querySelectorAll("#menuuuu");
let contentss = document.querySelector(".height-full-viewport");
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
/*---------------------render Page----------------------*/
