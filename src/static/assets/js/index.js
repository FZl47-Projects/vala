
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


/*------------------- add azmayesh --------------------*/
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
  successAlert("success","درخواشت شما ثبت شد")
});
/*------------------- add azmayesh --------------------*/

/*------------------- comment handler --------------------*/
console.log(JSON.parse(localStorage.getItem("user")));
window.addCommentPost = async (id, index) => {
  const commentInserts = [...document.querySelectorAll(".comment-input")];

  const data = {
    user: JSON.parse(localStorage.getItem("user")),
    text: commentInserts[index].value,
    post: id,
    accepted: false,
  };

  await toast("کامنت با موفقیت ارسال شد و در حال بررسی است")

  await sendComment(data);
  window.location.reload()
};
/*------------------- comment handler --------------------*/


/* ------------------- Logout btn -------------------- */
const exitBTN  = document.querySelector("#exit")
exitBTN.addEventListener('click',()=>{
  localStorage.removeItem("user")
  location.href="./sign-up.html"
})