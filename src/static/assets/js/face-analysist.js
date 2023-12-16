
import { analyze } from "./api/analyze.js";
import { getDataLocal } from "./helper.js";
const userId = await getDataLocal("user");


const PictureOne = document.querySelector("#picture-post-add-one");
const PictureTwO = document.querySelector("#picture-post-add-two"); 
const PictureTtee = document.querySelector("#picture-post-add-tree");
const SendBtn = document.querySelector("#finish");
SendBtn.addEventListener("click", async () => {
  var formdata = new FormData();
  formdata.append("image1", PictureOne.files[0], PictureOne.value);
  formdata.append("image2", PictureTwO.files[0], PictureTwO.value);
  formdata.append("image3", PictureTtee.files[0], PictureTtee.value);
  formdata.append("user", userId);


  
  var requestOptions = {
    method: "POST",
    body: formdata,
    redirect: "follow",
  };
  await analyze(requestOptions);
});


























const step_two = document.querySelector("#step-2");
const step_tree = document.querySelector("#step-3");
const content_one = document.querySelector("#upload-step-1");
const content_two = document.querySelector("#upload-step-2");
const content_tree = document.querySelector("#upload-step-3");
step_two.addEventListener("click", () => {
    content_two.classList.add("active");
    content_one.classList.remove("active");

  });

  step_tree.addEventListener("click", () => {
    content_tree.classList.add("active");
    content_two.classList.remove("active");
  });



