import { addUser } from "./api/signandlogin.js";

import { getDataLocal, getUserLocalStorage, phoneHandler } from "./helper.js";
import { toast } from "./toastify.js";




/* ------------------change step and content--------------------- */
let btn_step_2 = document.querySelector("#btn-step-2");
let btn_step_3 = document.querySelector("#btn-step-3");
let content_step_1 = document.querySelector("#content-step-1");
let content_step_2 = document.querySelector("#content-step-2");
let content_step_3 = document.querySelector("#content-step-3");

btn_step_2.addEventListener("click", () => {
  content_step_1.classList.remove("active");
  content_step_2.classList.add("active");
});
btn_step_3.addEventListener("click", () => {
  content_step_2.classList.remove("active");
  content_step_3.classList.add("active");
});

/* ------------------change step and content--------------------- */

/*----------------------active question------------------------*/

const answers = [...document.querySelectorAll(".answer-item")];

answers.forEach((item, index) => {
  item.addEventListener("click", () => {
    answers.forEach((item) => {
      item.classList.remove("active");
    });

    answers[index].classList.add("active");
  });
});

/*----------------------active question------------------------*/

/*---------------------------send information------------------------------ */
const btnSends = document.querySelectorAll(".next-level-btn");
const btnSendInformation = btnSends[btnSends.length - 1];
const birthday = document.querySelector("#birthday");
const weight = document.querySelector("#weight");
const name = document.querySelector("#name");
const image = document.querySelector("#javaz");
const height = document.querySelector("#height");

const answerQueiz = (data) => {
  const findItem = data.find((item) => item.className === "answer-item active");
  const result = findItem.getAttribute("data-count");

  return result;
};

btnSendInformation.addEventListener("click", async () => {
  if (!weight.value || !birthday.value || !height.value || !name.value) {
    await toast("لطفا تمام اطلاعات خواسته شده را وارد کنید");
  }

  if (!Boolean(image.value)) {
    await toast("لطفا پروفایل خود را وارد کنید");
  }



var dob = new Date(birthday.value); 
//calculate month difference from current date in time 
var month_diff = Date.now() - dob.getTime(); 

//convert the calculated difference in date format 
var age_dt = new Date(month_diff); 

//extract year from date 
var year = age_dt.getUTCFullYear(); 

//now calculate the age of the user 
var age = Math.abs(year - 1970); 

//display the calculated age 


const data = await getDataLocal("sign")


  var formdata = new FormData();
  formdata.append("profileimage", image.files[0], image.value);
  // formdata.append("queiz", +answerQueiz(answers) || 1);
  formdata.append("age", age);
  formdata.append("weight", weight.value);
  formdata.append("height", height.value);
  formdata.append("birthday", birthday.value);
  formdata.append("name", name.value);
  formdata.append("phone_number", phoneHandler(data.phoneNumber));
  formdata.append("nationalcode", 2981304021);
  formdata.append("wallet", 0);
  formdata.append("password", data.password);
  // formdata.append("confirmPassword", data.confirmPassword);


  var requestOptions = {
    method: "POST",
    body: formdata,
    redirect: "follow",
  };




  //زمانی که ثبت نام ایجاد شد
  const result = await addUser(requestOptions);
  console.log(result);
  window.localStorage.removeItem("sign")
  window.location.replace("./sign-up.html");
});
