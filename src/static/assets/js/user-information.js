import { successAlert } from "./Services.js";
import { getUserWithId, updateUser } from "./api/user.js";
import { getDataLocal } from "./helper.js";


/*----------------render Page---------------------*/

const userId = await getDataLocal("user");
const user = await getUserWithId(+userId);
const renderPage = async () => {
  const { name, birthday, weight, height, id, profileimage, phone_number } =
    user;

  const container = document.querySelector("#container");
  const titleContainer = document.querySelector("#title-container");
  const noteOne = `
  <div class="imge-user-profile col-6">
                               <img src="http://185.255.89.163:8000${profileimage}" alt="">
                                </div>
                                
                                <div class="col-6 name-user">
                                    <div>
                                        ${name}
                                    </div>

                                </div>
                                <span class="upload-image"> <img src="./assets/images/icon-valla/+.png" alt=""></span>`;
  const note = `
    <div class="col-12 p-2">
                                <label for="name-user" class="title">نام
                                   </label>
                                <div class="information-item">
                                    <input type="text" value="${name}" class="item-user"
                                        id="name" name="name-user">
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            
                            <div class="col-12 p-2">
                                <label for="name-user" class="title">تاریخ تولد
                                   </label>
                                <div class="information-item">
                                    <input type="date" value="${birthday}" class="item-user"
                                        id="birthday" name="phone-number-user">
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            <div class="col-12 p-2">
                                <label for="name-user" class="title">شماره همراه
                                   </label>
                                <div class="information-item">
                                    <input type="text" value="${phone_number}" class="item-user"
                                       id="phone" >
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            <div class="col-12 p-2">
                                <label for="name-user" class="title">قد
                                   </label>
                                <div class="information-item">
                                    <input type="text" value="${height}" class="item-user"
                                        id="height">
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            <div class="col-12 p-2">
                                <label for="name-user" class="title">وزن
                                   </label>
                                <div class="information-item">
                                    <input type="text" value="${weight}" class="item-user"
                                    id="weight" >
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            <div class="col-12 p-2">
                                <label for="name-user" class="title">رمزعبور
                                   </label>
                                <div class="information-item">
                                    <input type="password" value="23123654" class="item-user"
                                       id="password" >
                                        <span><img src="./assets/images/icon-valla/edit.png" alt=""></span>
                                </div>
                                
                            </div>
                            

                            <div class="btn-sabt" onclick="sabtHandler(${id})">
                                <span class="col-3">ثبت </span>
                        </div>`;
  container.innerHTML += note;
  titleContainer.innerHTML += noteOne;
};

await renderPage();
/*----------------render Page---------------------*/




/*------------------sabt handler-------------------*/
window.sabtHandler = async (id) => {
  const name = document.querySelector("#name").value;
  const birthday = document.querySelector("#birthday").value;
  const weightU = document.querySelector("#weight").value;
  const height = document.querySelector("#height").value;
  const password = document.querySelector("#password").value;
  const phone = document.querySelector("#phone").value;

  const data = {
    name,
    birthday,
    weight: weightU,
    height,
    phone_number: phone,
  };

 console.log(await updateUser(id, data))
 successAlert("success","تغییرات با موفقیت انجام شد ")
 setTimeout(() => {
  location.reload()
 }, 3000);
};
/*------------------sabt handler-------------------*/
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
