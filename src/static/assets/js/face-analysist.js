
const steps_one = document.querySelectorAll(".step-1");
const steps_two = document.querySelectorAll(".step-2");
const steps_three = document.querySelectorAll(".step-3");
const steps_four = document.querySelectorAll(".step-4");
const content_one = document.querySelector("#upload-step-1");
const content_two = document.querySelector("#upload-step-2");
const content_three = document.querySelector("#upload-step-3");
const content_four = document.querySelector("#upload-step-4");

steps_one.forEach((item, index) => {
    item.addEventListener("click", () => {
        content_one.classList.add("active");
        content_two.classList.remove("active");
        content_three.classList.remove("active");
        content_four.classList.remove("active");
    })
});

steps_two.forEach((item, index) => {
    item.addEventListener("click", () => {
        if ($('#upload-step-1 input[type=file]')[0].files.length === 0) {
            Toast.fire({
                icon: 'error',
                title: 'لطفا تصویر را آپلود کنید',
                timer: 3000
            });
            return
        }

        content_one.classList.remove("active");
        content_two.classList.add("active");
        content_three.classList.remove("active");
        content_four.classList.remove("active");
    })
});

steps_three.forEach((item, index) => {
    item.addEventListener("click", () => {
        if ($('#upload-step-2 input[type=file]')[0].files.length === 0) {
            Toast.fire({
                icon: 'error',
                title: 'لطفا تصویر را آپلود کنید',
                timer: 3000
            });
            return
        }

        content_one.classList.remove("active");
        content_two.classList.remove("active");
        content_three.classList.add("active");
        content_four.classList.remove("active");
    })
});

steps_four.forEach((item, index) => {
    item.addEventListener("click", () => {
        if ($('#upload-step-3 input[type=file]')[0].files.length === 0) {
            Toast.fire({
                icon: 'error',
                title: 'لطفا تصویر را آپلود کنید',
                timer: 3000
            });
            return;
        }

        content_one.classList.remove("active");
        content_two.classList.remove("active");
        content_three.classList.remove("active");
        content_four.classList.add("active");
    })
});


// ------------------------------ Set image on change input -----------------------------
function displayImage(event) {
    let fileInput = event.target;
    let file = fileInput.files[0];

    if (file) {
        let reader = new FileReader();
        reader.onload = function (e) {
            let selectedImage = document.getElementById(fileInput.name);
            selectedImage.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
}
