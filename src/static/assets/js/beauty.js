import { getUserWithId } from "./api/user.js";
import { getDataLocal } from "./helper.js";
import { baseUrl } from "./api/baseUrl.js"
import{sendReserveMoshavereh} from "./api/reserve.js"
/*------------------render Page----------------------*/
const userId = await getDataLocal("user");
const user = await getUserWithId(+userId);
const base =await  baseUrl()
console.log(base);
const renderPage = async() =>{

  const container = document.querySelector("#header-profile")
  const note = `<div class="profile">
  <div class="col-6 col-md-5 imge-user-profile">
    <div class="col-12">
      <img src="http://185.255.89.163:8000${user.profileimage}" alt="">
    </div>
  </div>
</div>

<div class="name-user">
  ${user.name}
</div>`

  container.innerHTML += note
}

await renderPage()

/*------------------render Page----------------------*/

/*-------------------show Modal Moshavereh----------------------*/
const btnShowModalM = document.querySelector("#btn-moshavereh");
const closeModal = document.querySelector("#modal-moshavereh .inner-modal");
const closeModalM = document.querySelector(".close-modal-adamtaeiid");
const modalM = document.querySelector("#modal-moshavereh");
btnShowModalM.addEventListener("click", () => {
  modalM.classList.add("active");
});
closeModal.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal") {
    modalM.classList.remove("active");
  }
});
closeModalM.addEventListener("click", (e) => {
  modalM.classList.remove("active");
});
/*-------------------show Modal Moshavereh----------------------*/
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

btnsShowModalrotin.forEach((item) => {
  item.addEventListener("click", () => {
    contentModalsrotin.classList.add("active");
  });
});

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

btnsShowModalazmayesh.forEach((item) => {
  item.addEventListener("click", () => {
    contentModalsazmayesh.classList.add("active");
  });
});

btnsCloseModalazmayesh.addEventListener("click", () => {
  contentModalsazmayesh.classList.remove("active");
});

contentModalsazmayesh.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal")
    contentModalsazmayesh.classList.remove("active");
});

/*----------------------------(show , close , send) modal add-post --------------------------- */

/*-------------------add azmayesh--------------------*/

const btnAddAzmayesh = document.querySelector("#btn-add-azmayesh");
btnAddAzmayesh.addEventListener("click", async () => {
  const id = JSON.parse(window.localStorage.getItem("user"));
  const element = document.querySelector(`#file-azmayesh`);
  const des = document.querySelector(`#des-azmayesh`);
  var formdata = new FormData();

  formdata.append("image", element.files[0], element.value);
  formdata.append("user", `${id}`);
  formdata.append("descripton", des.value);
  formdata.append("response", "response");

  var requestOptions = {
    method: "POST",
    body: formdata,
    redirect: "follow",
  };

  await addAzmayesh(requestOptions);
});

/*-------------------add azmayesh--------------------*/
const moshaverehname = document.querySelector("#name-moshavereh")
moshaverehname.innerHTML = user.name
const descriptionMoshavereh = document.querySelector("#moshavereh-description")
const submitMoshavereh = document.querySelector("#submit-moshavereh")
submitMoshavereh.addEventListener('click',async()=>{
  const data={
    "user":user.id,
    "description":descriptionMoshavereh.value,
      "accept": false,
      "types": "admin",
      "oprator":1
  
  }
await sendReserveMoshavereh(data)
location.reload()
})