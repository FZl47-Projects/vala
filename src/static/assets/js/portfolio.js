import { getManager } from "./api/managers.js";
import { getPostWithOp } from "./api/post.js";
import { sendReserve } from "./api/reserve.js";
import { getDataLocal, getId, getPath } from "./helper.js";
import{sendServiceComment,getServiceCommentWithOPID} from "./api/comment.js"
import{successAlert} from "./Services.js"
const id = await getId(window.location.search);
console.log(id);

/*-----------------render page------------------*/
const renderPage = async () => {
  const manager = await getManager(id);
 
  const containerTitle = document.querySelector("#container-title");
  const containerPost = document.querySelector("#container-portfolio");
  const footer = document.querySelector("#footer");

  const postO = await getPostWithOp(+id);
console.log(postO);

  postO.forEach((item) => {
    const isPod = postO.find((elem) => item.types === "podcast");
    console.log(!!isPod);

    const note = `

        <div class="content-modal modal-portfolio">

        <div div class="inner-modal d-flex flex-column">
          <div class="portifilo">
            <div class="btn-close m-2" style="cursor:pointer;">
              <img src="./assets/images/icon-valla/close-modal.png" alt="">
            </div>
            <div class="image-portifilo">
              <div class="d-flex justify-content-between align-items-center flex-column">
              <img src="${item.poster}" />
              ${
                !!isPod
                  ? `<audio controls class="my-2"><source src='${item.file}'  type='audio/mpeg' ></audio>`
                  : ""
              }
              </div>
              
            </div>
            <div class="title text-center " style="font-size : 24px">
                ${item.description}
            </div>
          </div>
        </div>
  
      </div>
        <div class="col-6 col-md-2 p-3 portfolio-items">
                <div class="portfolio-item">
                  <img src=${isPod ? item.poster : item.file} alt="">
                </div>
                <div class="title-portfolio-item">عنوان پست</div>

              </div>
        
        `;
    containerPost.innerHTML += note;
  });

  const titlePage = `
    <div class="category-user-inner col-6">
              <!-- imge-user -->
              <div class="col-6 col-md-2 p-3">
                <div class="imge-user">
                  <img src="http://185.255.89.163:8000${manager.image}" alt="">
                </div>
              </div>
              <!-- imge-user -->
              <!-- name-user -->
              <div class="col-6 col-md-10 p-3 jj">
                <div class="name-user">
               ${manager.name}

                </div>
              </div>
              <!-- name-user -->
            </div>
    `;
  const footerManager = `
    <div class="inner-reservation">
              <div class="right">
                <div class="title">خدمات</div>
                <div class="description">${manager.types}</div>

              </div>

              <div class="price">
                یک میلیون<br />
                تومان

              </div>
              <div class="btn-reserv" onclick="showModal()">
                رزرو
              </div>
            </div>`;
  containerTitle.innerHTML = titlePage;
  footer.innerHTML = footerManager;
};

await renderPage();
/*-----------------render page------------------*/

// -----------------------------------edit-post-itsm-----------------------------------//
let portfolio_item = document.querySelectorAll(".portfolio-items");
let modal_portfolio = document.querySelectorAll(".modal-portfolio");
let overalyModals = document.querySelectorAll(".modal-portfolio .inner-modal");
let closeModals = document.querySelectorAll(".btn-close");

portfolio_item.forEach((item, index) => {
  item.addEventListener("click", () => {
    modal_portfolio[index].classList.add("active");
  });
});
overalyModals.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal") {
      modal_portfolio[index].classList.remove("active");
    }
  });
});
closeModals.forEach((item, index) => {
  item.addEventListener("click", () => {
    modal_portfolio[index].classList.remove("active");
  });
});
// -------------------------------------edit-post-itsm---------------------------------//

/*-------------------show modal btn--------------------*/

window.showModal = () => {
  document.querySelector(".modal-reserve").classList.add("active");
};
const btnCloseModal = document.querySelector(".modal-reserve .inner-modal");
btnCloseModal.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal") {
    document.querySelector(".modal-reserve").classList.remove("active");
  }
});

/*-------------------show modal btn--------------------*/

/*-------------------reserve btn--------------------*/

const opratorId = await getPath(window.location.search);
const userId = await getDataLocal("user");
const modal = document.querySelector("#des-reserve");
console.log(modal)
const btnSend = document.querySelector("#btn-send");
btnSend.addEventListener("click", async () => {
  const data = {
    user: userId,
    oprator: +opratorId,
    description: modal.value,
    price: "0",
  };

  const result = await sendReserve(data);
  console.log(result)
  location.reload()
});

/*-------------------reserve btn--------------------*/
/*----------------------------(show , close , send) modal add-post --------------------------- */
/* ------------------change img and content--------------------- */
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

// send comment
const SubmitComment = document.querySelector("#submitComment")
SubmitComment.addEventListener('click',async()=>{
  const textComment = document.querySelector("#textComment")
  console.log(textComment.value);
  const data = {
    "text": textComment.value,
    "accepted": false,
    "user":localStorage.getItem("user"),
    "manager": id
}
console.log(await sendServiceComment(data));
successAlert("success","کامنت شما با موفقیت ثبت شد!")
setTimeout(()=>{
location.reload();
},3000)
})



const renderComment = async()=>{
  let  comment = await getServiceCommentWithOPID(id)
  // comment = comment.filter(item=>item.accepted
  //   == false)
  console.log(comment);
  comment.forEach(item=>{
    console.log(item);
    const note = `
    <div class="col-12 col-lg-8 ">
              <div class="comment-item">
                <!-- Photo of each comment -->
                <div class="col-2 col-md-1 p-1">
                  <div class="imge-comment">
                    <img src="./assets/image/download (1).png" alt="">
                  </div>
                </div>
                <!-- Photo of each comment -->
                <!-- The textual content of each comment -->
                <div class="col-10 col-md-11 test-comment p-1">${item.text}</div>
                <!-- The textual content of each comment -->
              </div>
            </div>
    `
    document.querySelector(".commentt").innerHTML+=note
  })
}
await renderComment()