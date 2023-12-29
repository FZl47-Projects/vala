
// ------------------ change img and content --------------------- //
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
// ------------------change img and content--------------------- //
