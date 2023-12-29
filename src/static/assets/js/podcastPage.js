let btns = document.querySelectorAll(".post-item");
let contents = document.querySelectorAll(".content-post");

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
if (btns.length) {
    btns[0].classList.add("active");
    contents[0].classList.add("active");
}

document.addEventListener(
    "play",
    (e) => {
        let audios = document.querySelectorAll("audio");

        for (let i = 0; i < audios.length; i++) {
            if (audios[i] !== e.target) {
                audios[i].pause();
            }
        }
    },
    true
);


// --------------------------------- story -------------------------------------//
let story = document.querySelectorAll(".story_item");
let modal_story = document.querySelectorAll(" .modal-hilight-pro");
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
// ---------------------------------story-------------------------------------//

document.addEventListener(
    "play",
    (e) => {
        let audios = document.querySelectorAll("audio");

        for (let i = 0; i < audios.length; i++) {
            if (audios[i] !== e.target) {
                audios[i].pause();
            }
        }
    },
    true
);

let btnHamburger = document.querySelectorAll(".inner-content-post-two");
btnHamburger.forEach((item, index) => {
    item.addEventListener("click", () => {
        if (e.target.className === "" || e.target.className === "") return;
        btnHamburger[index].classList.toggle("active");
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
// --------------------------------- btn next/prev Highlight ------------------------------------- //

