/*------------------------play and stop slider------------------------*/
let play = false;
const timer = (name, inputName, step) => {
    const images = [...document.querySelector(name).children];
    images.forEach((item) => {
        item.classList.remove("active");
    });

    images[0].classList.add("active");
    let count = 0;

    const input = document.querySelector(inputName);
    input.value = 0;
    const time = setInterval(() => {
        // console.log(count);
        if (count === images.length - 1) return;
        count++;
        images.forEach((item, index) => {
            item.classList.remove("active");
        });
        images[count].classList.add("active");
        input.value = +input.value + 1;
        play = true;
        // console.log(play);
    }, 2500);
    window.stopHandler = () => {
        clearInterval(time);
    };
};

window.playHandler = (step) => {
    timer(`#content-image`, `#amount-cream`, step);
};

window.changeHanlder = (step) => {
    const input = document.querySelector(`#amount-cream`);

    const images = [...document.querySelector(`#content-image`).children];
    const count = input.value / +step;

    if (count === images.length) return;

    images.forEach((item) => {
        item.classList.remove("active");
    });

    images[count].classList.add("active");
};


/*------------------------play and stop slider------------------------*/
const btnShowModal = document.querySelector("#btn-show-modal");
const modal = document.querySelector(".modal-add-ravand");
const closeModal = document.querySelector(".modal-add-ravand .inner-modal");
btnShowModal.addEventListener("click", () => {
    modal.classList.add("active");
});
closeModal.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal" || e.target.className === "close") {
        modal.classList.remove("active");
    }
});


/* ------------------change img and content--------------------- */
let btnss = document.querySelectorAll("#menuuuu");
let contentss = document.querySelector(".height-full-viewport");
let close_btn = document.querySelector("#close");

//   btns.addEventListener("click", () => {
//       contents.classList.add("viewport");
//     });
btnss.forEach((item) => {
    item.addEventListener("click", () => {
        contentss.classList.add("viewport");
    });
});

close_btn.addEventListener("click", () => {
    contentss.classList.remove("viewport");
});
/*----------------------------(show , close , send) modal rotin --------------------------- */
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

/*----------------------------(show , close , send) modal rotin --------------------------- */
/*----------------------------(show , close , send) modal add-post --------------------------- */
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

/*----------------------------(show , close , send) modal add-post --------------------------- */

/*-------------------add azmayesh--------------------*/

const btnAddAzmayesh = document.querySelector("#btn-add-azmayesh");

btnAddAzmayesh.addEventListener("click", async () => {
    const id = JSON.parse(window.localStorage.getItem("user"));
    const element = document.querySelector(`#file-azmayesh`);
    const des = document.querySelector(`#des-azmayesh`);
    var formdata = new FormData();

    formdata.append("image", element.files[0], element.value);
    formdata.append("user", `${id}`);
    formdata.append("descripton", des.value);
    formdata.append("response", "response");

    var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow",
    };

    await addAzmayesh(requestOptions);
});

/*-------------------add azmayesh--------------------*/