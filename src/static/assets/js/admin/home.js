const loader = document.querySelector("#loader")
const body = document.querySelector("#body")

import { confirmComments, deleteComment, getAllComments } from "../api/comment.js";
import { addPost, deletePost,onDeletePost, editPost, getAllPost } from "../api/post.js";
import { addStory, getAllStory } from "../api/story.js";
import { validateLogin } from "../api/validateLoginAdmin.js";
import { shortTicket } from "../helper.js";
import{successAlert} from "../Services.js"



await validateLogin();

const comments = await getAllComments();

const renderPage = async () => {
  const allPosts = await getAllPost();
  console.log(allPosts);
  const posts = allPosts.filter((item) => item.types === "image");
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
</div>  
</div>`;

    containerStories.innerHTML += note;
    containerMoadals.innerHTML += note1;
  });


  posts.forEach(async (item, index) => {
    const commentsPost = comments.filter((element) => item.id === element.post);
    const filterComment = comments.filter((item) => item.accepted === false);
 
    const note = `
    <div class="post-item col-3 col-md-12 active">
    <div class="content-modal modal-edit-post">
    <div class="inner-modal">
      <form class="px-4 pt-2">
        <div class="py-2">
          <div class="title">
            <div class="close-modal-edit-post" style="cursor: pointer;"><img
                src="../assets/images/icon-valla/close-modal.png"
                alt=""></div>
            <div>ویرایش پست </div>
          </div>
          <div class="uploade-imge">
            <label for="add-image" class="add-post">
              <div class="item-upload">
                تصویر
              </div>
            </label>
            <input type="file" id="add-image" class="image-edit"  hidden>


          </div>
          <input type="text" class="title-edit  w-100 my-2 rounded-2 border-1 border-white text-white" style="border : 1px solid #fff; " /> 
          <textarea
            name="modal"
            class="input-modal des-edit"
            cols="30"
            rows="7"
            placeholder="${item.description}"></textarea>
        </div>
        <div class="btn-modal" onclick="editHandler(${item.id} , ${index})">
          <div class="btn-sabt-post">
            ثبت
          </div>
        </div>
      </form>
    </div>
  </div>
  <div class="col-12 col-md-4 col-lg-3 p-1 ">
          <div class="right-post-item ${item.isDelete ? "opacity-25" : null}">
            <img src="${item.file}" alt="">
          </div>
        </div>
        <div class="col-8 col-md-7 col-lg-8 p-1">
          <div class="left-post-item">
            <div class="title-post" >${
              item.title
            } <span class="display-6 text-danger" style="font-size:15px;width:100%;display:inline-block;">${item.isDelete ? "حذف شده" : ""
    }</span></div>
            <div class="des-post"> 
     ${shortTicket(item.description, 100)}...

            </div>
            <div class="d-flex align-items-center">
                    ${
                      !item.isDelete
                        ? `<span class="ms-2" style="cursor: pointer;" onclick="deleteHandler(${item.id})"><img
                        src="../assets/images/icon-valla/trash-icon.png" alt=""></span>`
                        : `<span class='text-white ' style='cursor : pointer' onclick='ondeleteHandler(${item.id})'>ondelete</span>`
                    }
                  
                  </div>

          </div>

        </div>
       `;

    const noteTwo = `
      <div class="content-post ${item.isDelete ? "opacity-50" : null}">
      <img src="${item.file}" alt=""
        class="imge-post">
      <div class="inner-content-post-two">
        <div class="line">
          <div class="row">
            <div class="col-2 icon">
              <div class="heart"> <img
                  src="../assets/images/icon-valla/heart.png" alt=""></div>
              <div class="comment"><img
                  src="../assets/images/icon-valla/comment.png" alt=""></div>
            </div>


            <div class="col-10 pt-3">
              <div class="up-content-post">
                <div class="title-post">${item.title}</div>
                <div class="description">
                 ${item.description}
                </div>
              </div>

            </div>
          </div>

          <div class="commentt">
          ${Object.keys(filterComment)
            .map((key) => {
              return `<div class="col-12">
              <div class="comment-item">
                <div class="col-2 col-md-1 p-1">
                  <div class="imge-comment">
                    <img src="http://185.255.89.163:8000${filterComment[key].user.profileimage}" alt="">
                  </div>
                </div>
                <div class="col-8 col-md-10 test-comment p-1 text-right">
                    ${filterComment[key].text}
                </div>
                <div class="col-2 col-md-1">
                      <div class="p-2">
                        <div class="text-success text-center font-weight-bold m-1  rounded btns-post"
                        style="cursor: pointer; background-color: #e3dadad1;" onclick="confirmHandler(${filterComment[key].pk})">تایید</div>
                      <div class="text-danger text-center font-weight-bold m-1  rounded btns-post"
                      onclick="commentDelete(${filterComment[key].pk})"   style="cursor: pointer; background-color: #e3dadad1;">حذف</div>
                      </div>
                  </div>
              </div>
            </div>`;
            })
            .join("")}
            
            
            
            
            
            
            


          </div>




        </div>

      </div>
    </div>`;

    containerPosts.innerHTML += note;
    containerBigPost.innerHTML += noteTwo;
    loader.style.display = "none"
    body.style.display = "block"
  });
  // ---------------------------------change-post-content-post-------------------------------------//

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
    // ---------------------------------change-post-content-post-------------------------------------//

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

/*-------------------add post-----------------*/
const btnsShowModal = document.querySelector("#show-post");
const btnsCloseModal = document.querySelector(".close-modal-add-post");
// const btnsSendModal = document.querySelector(".btn-send-modal");
const contentModals = document.querySelector(".modal-add-post");

btnsShowModal.addEventListener("click", () => {
  contentModals.classList.add("active");
});

btnsCloseModal.addEventListener("click", () => {
  contentModals.classList.remove("active");
});
contentModals.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal")
    contentModals.classList.remove("active");
});


/*-------------------add post-----------------*/
const btnAddPost = document.querySelector("#add-post");
const imageAddPost = document.querySelector("#picture-post-add");
const textAddPost = document.querySelector("#text-post-add");
const titleAddPost = document.querySelector("#title-post-add");
btnAddPost.addEventListener("click", async () => {
  var formdata = new FormData();
  formdata.append("file", imageAddPost.files[0], imageAddPost.value);
  formdata.append("poster", imageAddPost.files[0], imageAddPost.value);
  formdata.append("description", textAddPost.value);
  formdata.append("like", 0);
  formdata.append("title", titleAddPost.value);
  formdata.append("types", "image");
  formdata.append("category", 1);
  formdata.append("oprator", JSON.parse(localStorage.getItem("user-admin")));
  var requestOptions = {
    method: "POST",
    body: formdata,
    redirect: "follow",
  };
  console.log(await addPost(requestOptions));
  successAlert("success","پست جدید ثبت شد!")
  setTimeout(()=>{
    location.reload()
  },3000)
});
/*-------------------add post-----------------*/



/*-------------------show Modal hilight-----------------*/
const btnsShowModal_b = document.querySelector("#add-highlit");
const btnsCloseModal_b = document.querySelector(".close-modal-add-hi");
// const btnsSendModal_b = document.querySelector(".btn-send-modal");
const contentModals_b = document.querySelector(".modal-add-highlit");

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

btnAddStory.addEventListener("click", async () => {
  await addStory("file-story", titleHilight.value);
});
/*-------------------add story-----------------*/

/*------------------------------Render Page--------------------------------- */

let btnHamburger = document.querySelectorAll(".inner-content-post-two");
btnHamburger.forEach((item, index) => {
  item.addEventListener("click", () => {
    btnHamburger[index].classList.toggle("active");
  });
});


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
// const btnsShowModalazmayesh = document.querySelectorAll("#azmayesh-raygan");
// const btnsCloseModalazmayesh = document.querySelector("#close-modal-azmayesh");
// const contentModalsazmayesh = document.querySelector(".modal-azmayesh-raygan");

// btnsShowModalazmayesh.forEach((item) => {
//   item.addEventListener("click", () => {
//     contentModalsazmayesh.classList.add("active");
//   });
// });

// btnsCloseModalazmayesh.addEventListener("click", () => {
//   contentModalsazmayesh.classList.remove("active");
// });

// contentModalsazmayesh.addEventListener("click", (e) => {
//   if (e.target.className === "inner-modal")
//     contentModalsazmayesh.classList.remove("active");
// });
/*----------------------------(show , close , send) modal add-post --------------------------- */


// -----------------------------------edit-post-itsm-----------------------------------//
let edit_btn = document.querySelectorAll(".edit-post");
let modal_edit = document.querySelectorAll(" .modal-edit-post");
let overalyModals = document.querySelectorAll(" .modal-edit-post .inner-modal");
let closeModals = document.querySelectorAll(".close-modal-edit-post");

edit_btn.forEach((item, index) => {
  item.addEventListener("click", () => {
    modal_edit[index].classList.add("active");
  });
});
overalyModals.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal") {
      modal_edit[index].classList.remove("active");
    }
  });
});
closeModals.forEach((item, index) => {
  item.addEventListener("click", () => {
    modal_edit[index].classList.remove("active");
  });
});
// -------------------------------------edit-post-itsm---------------------------------//

window.confirmHandler = async (id) => {
  const data = {
    accepted: true,
  };

  await confirmComments(data, id);
  window.location.reload()
};

window.editHandler = async (id , index) => {
  const titleEdit = [...document.querySelectorAll(".title-edit")][index];
  const desEdit = [...document.querySelectorAll(".des-edit")][index];
  const image = [...document.querySelectorAll(".image-edit")][index]; 

  var formdata = new FormData();
  if (!!titleEdit.value && !!image.value && !!desEdit.value) {
    formdata.append("title", titleEdit.value);
    formdata.append("description", desEdit.value);
    formdata.append("file", image.files[0], image.value);
    formdata.append("poster", image.files[0], image.value);
    console.log("one");
  } else if (!!desEdit.value && !!image.value) {
    formdata.append("description", desEdit.value);
    formdata.append("file", image.files[0], image.value);
    formdata.append("poster", image.files[0], image.value);
    console.log("two");
  } else if (!!titleEdit.value && !!image.value) {
    formdata.append("title", titleEdit.value ? titleEdit.value : title);
    formdata.append("file", image.files[0], image.value);
    formdata.append("poster", image.files[0], image.value);
  } else if (!!titleEdit.value && !!desEdit.value) {
    formdata.append("title", titleEdit.value);
    formdata.append("description", desEdit.value);
    console.log("three");
  } else if (!!titleEdit.value) {
    formdata.append("title", titleEdit.value);
  } else if (!!desEdit.value) {
    formdata.append("description", desEdit.value);
  } else if (!!image.value) {
    formdata.append("file", image.files[0], image.value);
    formdata.append("poster", image.files[0], image.value);
  }
  var requestOptions = {
    method: "PATCH",
    body: formdata,
    redirect: "follow",
  };

  await editPost(requestOptions, id);
  window.location.reload()
};

window.deleteHandler = async (id) => {
  const data = {
    isDelete: true,
  };
  console.log(id);
  await deletePost(id, data);
  successAlert("success","پست مورد نظر با موفقیت حذف شد")
  setTimeout(()=>{
    location.reload()
  },3000)
};

window.ondeleteHandler = async(id) => {
  const res = {
    isDelete: false,
  };

  await onDeletePost(id, res);
  successAlert("success","درخواست شما با موفقیت انجام شد")
  setTimeout(()=>{
    location.reload()
  },3000)
};

window.commentDelete = async(id) =>{
  
  await deleteComment(id)
}


