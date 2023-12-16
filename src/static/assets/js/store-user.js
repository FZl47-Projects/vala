import { getAllProduct ,InsertOrder} from "./api/store.js";
import { shortTicket } from "./helper.js";
import { successAlert } from "./Services.js";
const renderPage = async () => {
  const allProduct = await getAllProduct();
  const container = document.querySelector("#container-product");
  allProduct.forEach((item) => {
    const note = `
    <div class="col-12 col-md-3 col-lg-2
    product-item">
    <div class="product-item-inner">
        <div class="image-product">
            <img
                src="${item.poster}"
                alt="">
        </div>
        <div class="down-product-item">
            <div class="title-product">${item.name}</div>
            <div class="discription-product">${shortTicket(item.description,60)}</div>
            <div class="price">
                <span>قیمت </span>
                <span>${item.price}تومان</span>
            </div>
        </div>
        <button id="add">اضافه کردن</button>
    </div>
</div>
    `
    const modal = `  <div class="content-modal" id="bbb">
    <div class="inner-modal">
        <div class="modal-product">
            <div id="close-modal-store">
                <img src="./assets/images/icon-valla/close-modal.png"
                    alt="">
            </div>
            <div class="product-modal-image"><img
                    src="${item.poster}"
                    alt=""></div>
            <div class="title">${item.name}</div>
            <div class="product-modal-discription">${item.description}</div>
            <div class="information-input">
            </div>
            <div class="sabt"  onclick="addOrder(${item.id})">ثبت</div>


        </div>
    </div>
</div>`
    document.querySelector("#modal").innerHTML +=modal
    container.innerHTML +=note;

  })
  


}
await renderPage();







window.addOrder=async(id)=>{
  const userid = localStorage.getItem("user")
  const data ={
    "user":userid,
    "product":id
  }
  console.log(await InsertOrder(data));
  successAlert("success","درخواست شما ثبت شد")
  setTimeout(()=>{
    location.reload();
  },3000)
}




const btnsShowModal = document.querySelectorAll("#add");
const btnsCloseModal = document.querySelectorAll("#close-modal-store");
const btnsSendModal = document.querySelectorAll(".btn-send-modal");
const valueModals = document.querySelectorAll(".input-modal");
const contentModals = document.querySelectorAll("#bbb");

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
