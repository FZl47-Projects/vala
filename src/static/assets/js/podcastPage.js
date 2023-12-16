import { addAzmayesh } from "./api/azmayesh.js";
import { getAllPost } from "./api/post.js";
import { getAllStory } from "./api/story.js";
import { getUserLocal } from "./api/validateLoginUser.js";
import { shortTicket } from "./helper.js";
await getUserLocal();
const renderPage = async () => {
  const allPosts = await getAllPost();
  const podcasts = allPosts.filter((item) => item.types === "podcast");
  const containerPosts = document.querySelector("#posts-container");
  const containerBigPost = document.querySelector("#big-container");
  const containerStories = document.querySelector("#container-story");
  const containerMoadals = document.querySelector("#container-modals");

  const allStories = await getAllStory();

  allStories.forEach((item, index) => {

    const note = ` 
    
    <div class="col-3 col-md-2 p-2 highlit-item story_item" >
    <div class="highlit-item-inner">
      <img src="${item.file}" alt="">
    </div>
    <div class="highlit-title">${shortTicket(
      "هایلایت",
      15
    )}...</div>
  </div>`;

    const note1 = `<div class="content-modal modal-hilight-pro">
  <div class="inner-modal d-flex flex-column ">
  <div class="btn-exit display-1 text-white">×</div>
  <div class="border-1 border-white rounded-4 overflow-hidden " >
  <img src="${item.file}" />
  </div>
 <p class="text-white text-justify my-4" style="font-size : 1.5em">${item.title}</p>
  <div class="text-white">
        <button class="display-1 mx-2 next" onclick="nextHandler(${index})"><</h1>
        <button class="display-1 mx-2 prev" onclick="prevHandler(${index})">></button>
  </div>
</div>
  
</div>`;

    containerStories.innerHTML += note;
    containerMoadals.innerHTML += note1;
  });

  podcasts.forEach((item, index) => {

    const note = ` <div class="post-item ">
      <div class="col-3 col-md-4 col-lg-3 p-1">
        <div class=" right-post-item">
          <img src="${item.poster}" alt="${item.title}">
        </div>
     
      </div>
      <div class=" col-8 col-md-7 col-lg-8 p-1 ">
        <div class=" left-post-item ">
          <div class="title-post">${item.title}</div>
          <div class="des-post">${item.description}</div>
          <div style="color:#fff;">${item.category.name}</div>
        </div>
        
      </div>
   `;

    const noteTwo = `<div class="content-post">
      <!-- imge-podcast -->
    <img src="${item.poster}" alt="${item.title}" class="imge-post">
    <div class="inner-content-post">
     <div class="title-podcast">
     ${item.title}
     </div>


     <!--audio  -->
     <div class="podcast">
      <audio controls  class="jj">
        <source src="${item.file}"  type="audio/mpeg" >
       </audio>
     </div>

    </div>




  </div>`;

    containerPosts.innerHTML += note;
    containerBigPost.innerHTML += noteTwo;
  });

  let btns = document.querySelectorAll(".post-item");
  let contents = document.querySelectorAll(".content-post");

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
  if (btns.length) {
    btns[0].classList.add("active");
    contents[0].classList.add("active");
  }

  document.addEventListener(
    "play",
    (e) => {
      let audios = document.querySelectorAll("audio");
  
      for (let i = 0; i < audios.length; i++) {
        if (audios[i] !== e.target) {
          audios[i].pause();
        }
      }
    },
    true
  );
  


  // ---------------------------------story-------------------------------------//
  let story = document.querySelectorAll(".story_item");
  let modal_story = document.querySelectorAll(" .modal-hilight-pro");
  let overalyModals = document.querySelectorAll(
    ".modal-hilight-pro .inner-modal"
  );
  let closeModals = document.querySelectorAll(".btn-exit");

  story.forEach((item, index) => {
    item.addEventListener("click", () => {
      modal_story[index].classList.add("active");
    });
  });
  overalyModals.forEach((item, index) => {
    item.addEventListener("click", (e) => {
      if (e.target.className === "inner-modal d-flex flex-column ") {
        modal_story[index].classList.remove("active");
      }
    });
  });
  closeModals.forEach((item, index) => {
    item.addEventListener("click", () => {
      modal_story[index].classList.remove("active");
    });
  });
  // ---------------------------------story-------------------------------------//
};

await renderPage();
document.addEventListener(
  "play",
  (e) => {
    let audios = document.querySelectorAll("audio");

    for (let i = 0; i < audios.length; i++) {
      if (audios[i] !== e.target) {
        audios[i].pause();
      }
    }
  },
  true
);

/*------------------------------Render Page--------------------------------- */

let btnHamburger = document.querySelectorAll(".inner-content-post-two");
btnHamburger.forEach((item, index) => {
  item.addEventListener("click", () => {
    if (e.target.className === "" || e.target.className === "") return;
    btnHamburger[index].classList.toggle("active");
  });
});

/* ------------------change img and content--------------------- */
let btns = document.querySelectorAll(".post-item");
let contents = document.querySelectorAll(" .content-post");

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
/*----------------------------(show , close , send) modal add-post --------------------------- */
const btnsShowModal = document.querySelectorAll(".icon-add");
const btnsCloseModal = document.querySelectorAll(".close-modal-adamtaeid");
const btnsSendModal = document.querySelectorAll(".btn-send-modal");
const valueModals = document.querySelectorAll(".input-modal");
const contentModals = document.querySelectorAll(".modal-add-post");

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
/*----------------------------(show , close , send) modal add-post --------------------------- */
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

/*-------------------btn next , prev story-------------------*/

let modal_story = document.querySelectorAll(" .modal-hilight-pro");
let count;

window.prevHandler = (index) => {
  count = index;
  if (count + 1 === modal_story.length) return;
  modal_story.forEach((item) => {
    item.classList.remove("active");
  });

  modal_story[count + 1].classList.add("active");
};
window.nextHandler = (index) => {
  count = index;
  if (count === 0) return;
  modal_story.forEach((item) => {
    item.classList.remove("active");
  });
  modal_story[count - 1].classList.add("active");
};

/*-------------------btn next , prev story--------------------*/


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



