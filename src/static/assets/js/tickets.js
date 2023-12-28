
// ----------------- Show new ticket modal ------------------ //
const showModal = document.querySelector("#show-modal");
const modal = document.querySelector(".modal-add-ticket");
const closeModal = document.querySelector(".modal-add-ticket .inner-modal");

showModal.addEventListener("click", () => {
  modal.classList.add("active");
});
closeModal.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal") {
    modal.classList.remove("active");
  }
});
// ------------------- Show new ticket modal ----------------- //
