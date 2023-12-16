import { login ,addUser} from "./api/signandlogin.js";
import { removeUserLocal, setDataToLocal, setUserLocal } from "./helper.js";
import { successAlert } from "./Services.js";


/* ------------------change btn and content--------------------- */
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

// set errors
const setErrorTo = (input, message) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");

  formGroup.classList.add("error");
  small.innerText = message;
};

// set success
const setSuccessTo = (input) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");
  formGroup.classList.add("success");
  small.innerText = "";
};
