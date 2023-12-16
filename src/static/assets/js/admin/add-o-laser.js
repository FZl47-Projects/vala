import { addManager, addOLaser } from "../api/add-manager.js";
import { getAllManagers, getAllOLaser } from "../api/managers.js";
import { phoneHandler } from "../helper.js";
import { validateLogin } from "../api/validateLoginAdmin.js";
import { successAlert } from "../Services.js";
await validateLogin()

/*-----------------render Page ------------------*/

const renderPage = async () => {
  const allMangers = await getAllOLaser();
//   const filterManager = allMangers.filter((item) => item.types !== "admin");

  const containerManagers = document.querySelector("#container-managers");

  allMangers.forEach((item, index) => {
    {

      const note = `<div class="col-12 col-md-6 p-2">
    <a href="#">
      <div class="item-user">
        <div class="col-3 col-md-2">
          <div class="image-user">
            <img src="http://185.255.89.163:8000/media/8.png"
            alt="${item.name}">
          </div>
          </div>
          
        <div class="col-9 col-md-10 nnn ">
          <div class="name-user">
          ${item.name}         </div>
        </div>
      </div>
    </a>
    
  </div>`;

      containerManagers.innerHTML += note;
    }
  });
};

await renderPage();
/*-----------------render Page ------------------*/

/* ------------------change img and content--------------------- */
let btns = document.querySelectorAll(".btn-category-user");
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
/*----------------------------(show , close , send) modal add-food --------------------------- */
const btnsShowModall = document.querySelectorAll(".add-food-icon");
const btnsCloseModall = document.querySelectorAll(".close-modal-adamtaeid");
const btnsSendModall = document.querySelectorAll(".btn-send-modal");
const valueModalss = document.querySelectorAll(".input-modal");
const contentModalss = document.querySelectorAll(".modal-add-post");

btnsShowModall.forEach((item, index) => {
  item.addEventListener("click", () => {
    contentModalss[index].classList.add("active");
  });
});

btnsCloseModall.forEach((item, index) => {
  item.addEventListener("click", () => {
    contentModalss[index].classList.remove("active");
  });
});

contentModalss.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
      contentModalss[index].classList.remove("active");
  });
});
/*----------------------------(show , close , send) modal add-food --------------------------- */
/*----------------------------(show , close , send) modal answer --------------------------- */
const btnsShowModal = document.querySelectorAll(".btn-modal-1");
const btnsCloseModal = document.querySelectorAll(".close-modal-adamtaeid");
const btnsSendModal = document.querySelectorAll(".btn-send-modal");
const valueModals = document.querySelectorAll(".input-modal");
const contentModals = document.querySelectorAll(".modal-ticket");

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
/*----------------------------(show , close , send) modal modal answer --------------------------- */

/*----------------------------(show , close , send) modal more-text-ticket --------------------------- */
const btnsShowModaltwo = document.querySelectorAll("#more-btn");

const contentModalstwo = document.querySelectorAll(".modal-tickettwo");

btnsShowModaltwo.forEach((item, index) => {
  item.addEventListener("click", () => {
    contentModalstwo[index].classList.add("active");
  });
});

contentModalstwo.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
      contentModalstwo[index].classList.remove("active");
  });
});
/*----------------------------(show , close , send) modal more-text-ticket --------------------------- */

/*------------------------------add user ------------------------------*/

// const btnAddOprator = document.querySelector("#btn-add-oprator");
// const name = document.querySelector("#name");
// const age = document.querySelector("#age");
// const title = document.querySelector("#title");
// const image = document.querySelector("#image");

// btnAddOprator.addEventListener("click", async () => {
//   var formdata = new FormData();

//   formdata.append("image", image.files[0], image.value);
//   formdata.append("name", name.value);
//   formdata.append("types", "oprator");
//   formdata.append("age", age.value);

//   var requestOptions = {
//     method: "POST",
//     body: formdata,
//     redirect: "follow",
//   };

//   await addOprator(requestOptions);
// });

/*------------------------------add user ------------------------------*/

const btnShowModal = document.querySelector("#btn-show-modal-add");
const modalAdd = document.querySelector("#modal-add");
const closeModal = document.querySelector(".close-modal-add-post");

btnShowModal.addEventListener("click", () => {
  modalAdd.classList.add("active");
});

closeModal.addEventListener("click", () => {
  modalAdd.classList.remove("active");
});

/*-----------------btn add manager------------------*/
const btnAdd = document.querySelector("#btn-add-oprator");

const name = document.querySelector("#name");
const phone = document.querySelector("#phone");

btnAdd.addEventListener("click", async () => {
    const data = {
        name : name.value,
        phonenumber : phoneHandler(phone.value)
    }
    
    const res = {
        method : "POST",
        body : JSON.stringify(data),
        headers : {
            "Content-Type" : "application/json"
        }
    }

    await addOLaser(res)
    successAlert("success","اپراتور جدید افزوده شد ")
    setTimeout(() => {
location.reload();
    }, 3000);
});

/*-----------------btn add manager------------------*/
