
// ------------------ Change step and content --------------------- //
let btn_step_1 = document.querySelector("#btn-step-1");
let btn_step_2 = document.querySelector("#btn-step-2");
let btn_step_3 = document.querySelector("#btn-step-3");
let content_step_1 = document.querySelector("#content-step-1");
let content_step_2 = document.querySelector("#content-step-2");
let content_step_3 = document.querySelector("#content-step-3");

btn_step_1.addEventListener("click", () => {
  content_step_2.classList.remove("active");
  content_step_1.classList.add("active");
});

btn_step_2.addEventListener("click", () => {
  content_step_1.classList.remove("active");
  content_step_2.classList.add("active");
});

btn_step_3.addEventListener("click", () => {
  const inputs = [...content_step_2.querySelectorAll("input")];
  let isEmpty = false;

  inputs.forEach((item, index) => {
    if (item.value === '') {
      Toast.fire({
          icon: 'error',
          title: `لطفا مشخصات را وارد کنید`,
      });

      isEmpty = true;
    }
  })

  if (isEmpty) {
    return;
  }

  content_step_2.classList.remove("active");
  content_step_3.classList.add("active");
});
// ------------------ Change step and content --------------------- //


// ---------------------- active question ------------------------ //
const answers = [...document.querySelectorAll(".answer-item")];

answers.forEach((item, index) => {
  item.addEventListener("click", () => {
    answers.forEach((item) => {
      item.classList.remove("active");
    });

    answers[index].classList.add("active");
  });
});
// ---------------------- active question ------------------------ //


// --------------- Set user profile picture after select ----------------- //
function displayImage(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const selectedImage = document.getElementById('userProfilePic');
            selectedImage.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
}
// --------------- Set user profile picture after select ----------------- //
