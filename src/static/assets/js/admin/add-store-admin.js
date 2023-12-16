import { addProduct,getAllProduct } from "../api/store.js";
import { validateLogin } from "../api/validateLoginAdmin.js";
import { shortTicket } from "../helper.js";

await validateLogin();

const NameProduct = document.querySelector("#name-product")
const PriceProduct = document.querySelector("#price-product")
const DesProduct = document.querySelector("#des-product")
const PictureProduct= document.querySelector("#picture-product")
const SabtBtn = document.querySelector("#sabt-btn")


SabtBtn.addEventListener("click" ,async () =>{
    var formdata = new FormData()
    formdata.append("name", NameProduct.value);
    formdata.append("description", DesProduct.value);
    formdata.append("price", PriceProduct.value);
    formdata.append("poster", PictureProduct.files[0], PictureProduct.value);

    var requestOptions = {
      method: "POST",
      body: formdata,
      redirect: "follow",
    };
    await addProduct(requestOptions);




})
const renderPage = async () => {
  const allProduct = await getAllProduct();
  const container = document.querySelector("#container-admin");
  allProduct.forEach((item) => {
    const note = `
    <div class="col-12 col-md-4 col-lg-4
    product-item">
    <div class="product-item-inner">
        <div class="image-product">
            <img
                src="http://185.255.89.163:8000/${item.poster}"
                alt="">
        </div>
        <div class="down-product-item">
            <div class="title-product">${item.name}</div>
            <div class="discription-product">${shortTicket(item.description, 60)}</div>
            <div class="price">
                <span>قیمت </span>
                <span>${item.price}تومان</span>
            </div>
        </div>
        <button id="add">اضافه کردن</button>
    </div>
</div>
    `
    container.innerHTML +=note;
  })
  


}
await renderPage();


