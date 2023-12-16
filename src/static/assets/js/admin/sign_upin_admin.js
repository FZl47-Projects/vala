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
/* ------------------change btn and content--------------------- */


let form = document.querySelector(".form-login");
let phoneNumber = document.querySelector("#phoneNumber-login");
let password = document.querySelector("#password-login");

phoneNumber.focus();

// submit form
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  checkInput();
  if (checkInput() === false) {
    let userLogin = {
      phonenumber: `${phoneNumber.value}`,
      password: `${password.value}`,
    };

    const result = await login(userLogin);

    if (result === false || result === "" || result === undefined) {
      successAlert("error", "کاربر یافت نشد");
    }
    else{
      window.localStorage.setItem("user" , result)
      setTimeout(() => {
        window.location.replace("./index.html");
      }, 2000);
    }
  }
});

// validation inputs
const checkInput = () => {
  const phoneValue = phoneNumber.value.trim();
  const passwordValue = password.value.trim();
  let errors = {};
  if (phoneValue === "") {
    setError(phoneNumber, "لطفا شماره همراه خودرا وارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (checkPhoneNumber(`${phoneValue}`) === false) {
    setError(phoneNumber, "لطفا شماره همراه معتبر وارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(phoneNumber);
    delete errors.phoneNumber;
  }

  if (passwordValue === "") {
    setError(password, "لطفا رمز عبور خود را وارد کنید");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (passwordValue.length < 2) {
    setError(password, "رمز عبور نباید کمتر از هشت کاراکتر باشد");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(password);
    delete errors.password;
  }

  return !!Object.keys(errors).length;
};

// set errors
const setError = (input, message) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");

  formGroup.classList.add("error");
  small.innerText = message;
};

// set success
const setSuccess = (input) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");
  formGroup.classList.add("success");
  small.innerText = "";
};
// ------------------------------------------------------------------//












let form_operator = document.querySelector(".form-login-op");
let phoneNumber_operator = document.querySelector("#phoneNumber-login-op");
let password_operator = document.querySelector("#password-login-op");

phoneNumber_operator.focus();

// submit form
form_operator.addEventListener("submit", async (e) => {
  e.preventDefault();
  checkInput_operator();
  if (checkInput_operator() === false) {
    let userLogin = {
      phonenumber_operator: `${phoneNumber.value}`,
      password_operator: `${password.value}`,
    };

    const result = await login(userLogin);

    if (result === false || result === "" || result === undefined) {
      successAlert("error", "کاربر یافت نشد");
    }
    else{
      window.localStorage.setItem("user" , result)
      setTimeout(() => {
        window.location.replace("./index.html");
      }, 2000);
    }
  }
});

// validation inputs
const checkInput_operator = () => {
  const phoneValue = phoneNumber_operator.value.trim();
  const passwordValue = password_operator.value.trim();
  let errors = {};
  if (phoneValue === "") {
    setError(phoneNumber_operator, "لطفا شماره همراه خودراوارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (checkPhoneNumber(`${phoneValue}`) === false) {
    setError(phoneNumber_operator, "لطفا شماره همراه معتبر وارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(phoneNumber_operator);
    delete errors.phoneNumber;
  }

  if (passwordValue === "") {
    setError(password_operator, "لطفا رمز عبور خود را وارد کنید");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (passwordValue.length < 2) {
    setError(password_operator, "رمز عبور نباید کمتر از هشت کاراکتر باشد");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(password_operator);
    delete errors.password;
  }

  return !!Object.keys(errors).length;
};

// set errors
const setError_operator = (input, message) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");

  formGroup.classList.add("error");
  small.innerText = message;
};

// set success
const setSuccess_operator = (input) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");
  formGroup.classList.add("success");
  small.innerText = "";
};
// ------------------------------------------------------------------//

const btnAdmin = document.querySelector("#admin");
const btnOprator = document.querySelector("#oprator");

btnAdmin.addEventListener("click" , () =>{
  window.localStorage.setItem("user-admin" , JSON.stringify(1))
  window.location.replace("./index-admin.html")
})
btnOprator.addEventListener("click" , () =>{
  window.localStorage.setItem("user-admin" , JSON.stringify(2))
  window.location.replace("../Operator/index.html")
})