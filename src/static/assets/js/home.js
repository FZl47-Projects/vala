// --------------------------------- Highlights ------------------------------------- //
let story = document.querySelectorAll(".story_item");
let modal_story = document.querySelectorAll(".modal-hilight-pro");
let overalyModals = document.querySelectorAll(".modal-hilight-pro .inner-modal");
let closeModals = document.querySelectorAll(".btn-exit");

story.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_story[index].classList.add("active");
    });
});
overalyModals.forEach((item, index) => {
    item.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal d-flex flex-column ") {
            modal_story[index].classList.remove("active");
        }
    });
});
closeModals.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_story[index].classList.remove("active");
    });
});

// ------------------- btn next/prev Highlight ------------------- //
let count;

window.prevHandler = (index) => {
    count = index;
    if (count + 1 === modal_story.length) return;
    modal_story.forEach((item) => {
        item.classList.remove("active");
    });

    modal_story[count + 1].classList.add("active");
};

window.nextHandler = (index) => {
    count = index;
    if (count === 0) return;
    modal_story.forEach((item) => {
        item.classList.remove("active");
    });
    modal_story[count - 1].classList.add("active");
};
// --------------------------------- Highlights ------------------------------------- //


// ---------------------------------- Posts ----------------------------------------- //
let postsBtn = document.querySelectorAll(".post-item");
let contents = document.querySelectorAll(" .content-post");

postsBtn.forEach((item, index) => {
    item.addEventListener("click", () => {
        postsBtn.forEach((item) => {
            item.classList.remove("active");
        });
        contents.forEach((item) => {
            item.classList.remove("active");
        });
        postsBtn[index].classList.add("active");
        contents[index].classList.add("active");
    });
});

if (postsBtn.length) {
    postsBtn[0].classList.add("active");
    contents[0].classList.add("active");
}
// ------------------------------- Posts ----------------------------------------- //


// -------------------------- Posts description ---------------------------- //
let btnHamburger = document.querySelectorAll(".inner-content-post-two");

btnHamburger.forEach((item, index) => {
    item.addEventListener("click", (e) => {
        if (e.target.className === "" ||
            e.target.className === "comment-input" ||
            e.target.className === "btn-send" ||
            e.target.classList.contains("like-icon"))
            return;
        btnHamburger[index].classList.toggle("active");
    });
});
// ------------------------------- Posts description ---------------------------- //


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


// ---------------------------- Like Post handler -------------------------- //
function likePost(id, el) {
    $.get(`/post/${id}/like/`).then(response => {
        if (response['response'] === 'liked') {
            el.classList.replace("bi-heart", "bi-heart-fill");
        } else {
            el.classList.replace("bi-heart-fill", "bi-heart");
        }
    })
}
// ---------------------------- Like Post handler -------------------------- //

