// ------------------------------ Menu desk --------------------------- //
let btnss = document.querySelectorAll("#menuuuu");
let contentss = document.querySelector("#height-full-viewport-desk");
let close_btn = document.querySelector("#close");

btnss.forEach((item) => {
    item.addEventListener("click", () => {
        contentss.classList.add("viewport");
    });
});

close_btn.addEventListener("click", () => {
    contentss.classList.remove("viewport");
});
// ------------------------ Menu desk ------------------------------- //


// ---------------------------- Menu mobile -------------------------- //
let btnss_m = document.querySelectorAll("#menuuuu-b");
let contentss_m = document.querySelector("#height-full-viewport-mobile");
let close_btn_m = document.querySelector("#close-2");

btnss_m.forEach((item) => {
    item.addEventListener("click", () => {
        contentss_m.classList.add("viewport");
    });
});
close_btn_m.addEventListener("click", () => {
    contentss_m.classList.remove("viewport");
});
// --------------------------- Menu mobile ----------------------------- //
