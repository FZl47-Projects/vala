// ----------------------- Add highlight modal --------------------------- //
let btnsShowModal_b = document.querySelector(".add-story-btn");
let btnsCloseModal_b = document.querySelector('.close-modal-add-hi');
let contentModals_b = document.querySelector(".add-story-modal");

btnsShowModal_b.addEventListener("click", () => {
    contentModals_b.classList.add("active");
});
btnsCloseModal_b.addEventListener("click", () => {
    contentModals_b.classList.remove("active");
});
contentModals_b.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
        contentModals_b.classList.remove("active");
});
// ----------------------- Add highlight modal ----------------------- //


// ------------------- Add post modal ----------------- //
let btnsShowModal = document.querySelector("#show-modal-podcast");
let btnsCloseModal = document.querySelector(".close-modal-add-post");
let contentModals = document.querySelector(".add-post-modal");

btnsShowModal.addEventListener("click", () => {
    contentModals.classList.add("active");
});

btnsCloseModal.addEventListener("click", () => {
    contentModals.classList.remove("active");
});
contentModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal")
        contentModals.classList.remove("active");
});
// ------------------- Add post modal ----------------- //


// ---------------------------- Add data to delete modal -------------------------- //
$('#deletePodcastModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget)
    let primaryKey = button.data('primarykey')

    let modal = $(this)
    modal.find('.modal-body #podcastId').val(primaryKey)
})
// ---------------------------- Add data to delete modal -------------------------- //
