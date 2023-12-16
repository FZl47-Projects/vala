import {
  addRavand,
  addRoutin,
  getAllRavand,
  getAllRoutin,
  addImageRavand,
  getAllImageRavandWithUser,
} from "./api/routin.js";
import { getUserWithId } from "./api/user.js";
import { getDataLocal } from "./helper.js";
import{successAlert } from "./Services.js"

/*---------------------render page-----------------------*/
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id  = urlParams.get('id')
console.log(urlParams);
const userId = await getDataLocal("user");
const user = await getUserWithId(+userId);

const renderPage = async () => {
  const headerProfile = document.querySelector("#header-profile")
  console.log(user);
  const headerNote = `
  <!-- imge-user -->
            <div class="col-6 col-md-2 p-3">
              <div class="imge-user">
                <img src="http://127.0.0.1:8000${user.profileimage}" alt="">
              </div>
            </div>
            <!-- imge-user -->
            <!-- name-user -->
            <div class="col-6 col-md-10 p-3 jj">
              <div class="name-user">
                ${user.name}

              </div>
            </div>
            <!-- name-user -->
  `

headerProfile.innerHTML += headerNote;























  const container = document.querySelector("#content");

  const ravands = await getAllRavand();
  const ravandUser = ravands.filter((item) => item.user === +userId);
  let image =''
 if(id!=null)
   image = await getAllImageRavandWithUser(id);
  console.log(image);

  const note = `
 <div class="item-images-r" id="content-image">
    ${
      !image.length
        ? "<p class='display-6 text-white'>برای اضافه کردن عکس به روند بهبودی بروی + کلیک کنید</p>"
        : ""
    }
    ${Object.keys(image)
      .map((item) => {
        return `
        <img class="image" src="${image[item].image}" alt="image">
        `;
      })
      .join("")}


        
        
    </div>
      <div class=" col-12 col-lg-8 p-1" style="color: #fff;">
        <div class=" contenthh">
            <div class="name-user">${user.name}</div>
        <label id="title-type-range" for="amount-cream">روند بهبودی</label>
        <input id="amount-cream" type="range" value="0" min="0" max="${
          image.length - 1
        }" name="cream" list="amount" step="1" oninput="changeHanlder(${1})">
        <button class="btn-pl" onclick="playHandler(${1})">play</button>
        <button class="btn-pl" onclick="stopHandler()">stop</button>
        </div>
        
      </div>
    `;

  container.innerHTML = note;
  const images = [...document.querySelector(`#content-image`).children];
  
  if (ravandUser.length) {
    images[0].classList.add("active");
  }
};

await renderPage();

/*---------------------render page-----------------------*/

/*------------------------play and stop slider------------------------*/
let play = false;
const timer = (name, inputName, step) => {
  const images = [...document.querySelector(name).children];
  images.forEach((item) => {
    item.classList.remove("active");
  });

  images[0].classList.add("active");
  let count = 0;

  const input = document.querySelector(inputName);
  input.value = 0;
  const time = setInterval(() => {
    // console.log(count);
    if (count === images.length - 1) return;
    count++;
    images.forEach((item, index) => {
      item.classList.remove("active");
    });
    images[count].classList.add("active");
    input.value = +input.value + 1;
    play = true;
    // console.log(play);
  }, 2500);
  window.stopHandler = () => {
    clearInterval(time);
  };
};

window.playHandler = (step) => {
  timer(`#content-image`, `#amount-cream`, step);
};

window.changeHanlder = (step) => {
  const input = document.querySelector(`#amount-cream`);

  const images = [...document.querySelector(`#content-image`).children];
  const count = input.value / +step;

  if (count === images.length) return;

  images.forEach((item) => {
    item.classList.remove("active");
  });

  images[count].classList.add("active");
};


/*------------------------play and stop slider------------------------*/
const btnShowModal = document.querySelector("#btn-show-modal");
const modal = document.querySelector(".modal-add-ravand");
const closeModal = document.querySelector(".modal-add-ravand .inner-modal");
btnShowModal.addEventListener("click", () => {
  modal.classList.add("active");
});
closeModal.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal" || e.target.className === "close") {
    modal.classList.remove("active");
  }
});




// const allRoutin = await getAllRoutin();
// const isRoutin = allRoutin.find((item) => item.user === +userId);

// const btnSendRavand = document.querySelector("#btn-ravand");

// const notRotin = async () => {
//   const image = document.querySelector("#picture-ravand-add");
//   const data = {
//     name: "amir",
//     isActive: false,
//     value: "asdlknv;sa",
//     user: +userId,
//     types: "food",
//   };

//   const routin = await addRoutin(data);

//   await addRavand(requestOptions);
// };

// const routinA = async () => {
//   const image = document.querySelector("#picture-ravand-add");

//   var formData = new FormData();
//   formData.append("image", image.files[0], image.value);
//   formData.append("user", +userId);
//   formData.append("routin", isRoutin.id);
//   var requestOptions = {
//     method: "POST",
//     body: formData,
//     redirect: "follow",
//   };
//   await addRavand(requestOptions);
// };
// btnSendRavand.addEventListener("click", async () => {

//   if (!Boolean(isRoutin)) {
//     await notRotin();
//   } else {
//     await routinA();
//   }

//   window.location.reload()
// });




const InsertimageRavand = document.querySelector("#btn-ravand")

InsertimageRavand.addEventListener('click',async()=>{
if(id!=null){  console.log("hello");
  const image = document.querySelector("#picture-ravand-add")
  var formData = new FormData();
  formData.append("image", image.files[0], image.value);
  formData.append("ravand", id);

  var requestOptions = {
    method: "POST",
    body: formData,
    redirect: "follow",
  };
  console.log(addImageRavand(requestOptions))
  successAlert("success","با موفقیت ثبت شد ")
setTimeout(()=>{
  location.reload()
},3000)
}else{
const result = await addRavand({"user":localStorage.getItem("user")})
console.log(result);
const image = document.querySelector("#picture-ravand-add")
var formData = new FormData();
formData.append("image", image.files[0], image.value);
formData.append("ravand", result.id);

var requestOptions = {
  method: "POST",
  body: formData,
  redirect: "follow",
};
console.log(addImageRavand(requestOptions))
successAlert("success","با موفقیت ثبت شد ")
setTimeout(()=>{
  location.href=`./recovery-process.html?id=${result.id}`
},3000)
}
})















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