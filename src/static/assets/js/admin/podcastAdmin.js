import { addPodcast,GetPodcast,InsertPodcast} from "../api/podcast.js";
import { getAllPost } from "../api/post.js";
import { addStory, getAllStory } from "../api/story.js";
import { getUserLocalStorage } from "../helper.js";
import { getId, shortTicket } from "../helper.js";

import { validateLogin } from "../api/validateLoginAdmin.js";
await validateLogin()



const renderselect = async (material) => {
  material.forEach((item) => {
    const note = `<option value="${item.name}" style="color:white;" >${item.name}</option>`;
    document.querySelector("#select").innerHTML += note;
  });
};
const category = await GetPodcast();
await renderselect(category)

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
    <div class="highlit-title">${shortTicket(item.title , 15)}...</div>
  </div>`;

    const note1 = `<div class="content-modal modal-hilight-pro">
  <div class="inner-modal d-flex flex-column ">
  <div class="btn-exit display-1 text-white">×</div>
  <div class="border-1 border-white rounded-4 overflow-hidden " >
  <img src="${item.file}" />
  </div>
 <p class="text-white text-justify my-4" style="font-size : 1.5em">${item.title}</p>
    
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
        </div>
        
      </div>
      <div class="more" ><img
          src="../assets/images/icon-valla/MENUUU.png" alt=""></div>
    </div>`;

    const noteTwo = `<div class="content-post">
      <!-- imge-podcast -->
    <img src="${item.poster}" alt="${item.title}" class="imge-post">
    <div class="inner-content-post">
     <div class="title-podcast">
     ${shortTicket(item.title , 50)}
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
  // ---------------------------------story-------------------------------------//
 let story = document.querySelectorAll(".story_item");
 let modal_story = document.querySelectorAll(" .modal-hilight-pro");
 let overalyModals = document.querySelectorAll(
   " .modal-hilight-pro .inner-modal"
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

/*-------------------add post-----------------*/
const btnsShowModal_p = document.querySelector("#show-modal-podcast");
const btnsCloseModal_p = document.querySelector(".close-modal-add-podcast");
// const btnsSendModal_p = document.querySelector(".btn-send-modal");
const contentModals_p = document.querySelector("#modal-podcast");
  btnsShowModal_p.addEventListener("click", () => {
    contentModals_p.classList.add("active");
  });
  btnsCloseModal_p.addEventListener("click", () => {
    contentModals_p.classList.remove("active");
  });
  contentModals_p.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
    contentModals_p.classList.remove("active");
  })


  
  /*-------------------add post-----------------*/
const btnAddPodcast = document.querySelector("#add-podcast");
const imageAddPodcast = document.querySelector("#image-podcast");
const podcastAddPodcast = document.querySelector("#podcast");
const textAddPodcast = document.querySelector("#text-podcast-add");

const opratorId = await getUserLocalStorage("user-admin")


btnAddPodcast.addEventListener("click", async () => {
  const selectedcategory = document.querySelector("#Category-name").value
  let categoryId=category.filter(item=>item.name==selectedcategory);
  if(!categoryId.length){
    const categoryData={
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"name":selectedcategory})
    };
   
  
    const response = await InsertPodcast(categoryData)
   categoryId=response.id;
  }
  console.log(categoryId);
  var formdata = new FormData();
  formdata.append("file", podcastAddPodcast.files[0], podcastAddPodcast.value);
  formdata.append("poster", imageAddPodcast.files[0], imageAddPodcast.value);
  formdata.append("description", textAddPodcast.value);
  formdata.append("like", 0);
  formdata.append("types", "podcast");
  formdata.append("oprator", +opratorId);
  formdata.append("title",document.querySelector("#title").value)
  formdata.append("category",categoryId)
  var data = {
    method: "POST",
    body: formdata,
    redirect: "follow",
  };
  
  console.log(await addPodcast(data));
  location.reload()

});
/*-------------------add post-----------------*/

/*------------------------------Render Page--------------------------------- */

let btnHamburger = document.querySelectorAll(".inner-content-post-two");
btnHamburger.forEach((item, index) => {
  item.addEventListener("click", () => {
    btnHamburger[index].classList.toggle("active");
  });
});

/* ------------------change img and content--------------------- */

/* ------------------change img and content--------------------- */



/*-------------------show Modal hilight-----------------*/

const btnsShowModal_b = document.querySelector("#add-highlit");
const btnsCloseModal_b = document.querySelector(".close-modal-add-hi");
// const btnsSendModal_b = document.querySelector(".btn-send-modal");
const contentModals_b = document.querySelector("#modal-hilight");


btnsShowModal_b.addEventListener("click", () => {
  contentModals_b.classList.add("active");
});
btnsCloseModal_b.addEventListener("click", () => {
  contentModals_b.classList.remove("active");
});
contentModals_b.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal")
    contentModals_b.classList.remove("active");
});

/*-------------------show Modal hilight-----------------*/
/*-------------------add story-----------------*/
const btnAddStory = document.querySelector("#add-story");
const titleHilight = document.querySelector("#title-hilight");
console.log(btnAddPodcast);

btnAddStory.addEventListener("click", async () => {
  await addStory("add-image", titleHilight.value);
});
/*-------------------add story-----------------*/



/*---------------------btns next and prev story-------------------------*/
// const next = document.querySelector("#next")





/*---------------------btns next and prev story-------------------------*/






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
//   const btnsShowModalrotin = document.querySelectorAll("#icon-add-rotin");
//   const btnsCloseModalrotin = document.querySelector("#close-modal-rotin");
//   const contentModalsrotin = document.querySelector(".modal-rotin");

//   btnsShowModalrotin.forEach((item) => {
//     item.addEventListener("click", () => {
//       contentModalsrotin.classList.add("active");
//     });
//   });

//   btnsCloseModalrotin.addEventListener("click", () => {
//     contentModalsrotin.classList.remove("active");
//   });

//   contentModalsrotin.addEventListener("click", (e) => {
//     if (e.target.className === "inner-modal")
//       contentModalsrotin.classList.remove("active");
//   });
