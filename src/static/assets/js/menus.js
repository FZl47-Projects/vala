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


// ---------------------------- Modal routine --------------------------- //
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
// ---------------------------- Modal routine --------------------------- //


// ---------------------------- Modal Free test --------------------------- //
const btnsShowModalazmayesh = document.querySelectorAll("#azmayesh-raygan");
const btnsCloseModalazmayesh = document.querySelector("#close-modal-azmayesh");
const contentModalsazmayesh = document.querySelector(".modal-azmayesh-raygan");

btnsShowModalazmayesh.forEach((item) => {
    item.addEventListener("click", () => {
        contentModalsazmayesh.classList.add("active");
    });
});

btnsCloseModalazmayesh.addEventListener("click", () => {
    contentModalsazmayesh.classList.remove("active");
});

contentModalsazmayesh.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
        contentModalsazmayesh.classList.remove("active");
});
// ---------------------------- Modal Free test --------------------------- //
