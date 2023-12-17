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
            e.target.classList.contains("btn-send") ||
            e.target.classList.contains("like-icon"))
            return;
        btnHamburger[index].classList.toggle("active");
    });
});
// ------------------------------- Posts description ---------------------------- //


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

