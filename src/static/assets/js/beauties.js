
// ------------------- Modal Moshavereh ---------------------- //
const btnShowModalM = document.querySelector("#btn-moshavereh");
const closeModal = document.querySelector("#modal-moshavereh .inner-modal");
const closeModalM = document.querySelector(".close-modal-adamtaeiid");
const modalM = document.querySelector("#modal-moshavereh");

btnShowModalM.addEventListener("click", () => {
    modalM.classList.add("active");
});
closeModal.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal") {
        modalM.classList.remove("active");
    }
});
closeModalM.addEventListener("click", (e) => {
    modalM.classList.remove("active");
});
// ------------------- Modal Moshavereh ---------------------- //
