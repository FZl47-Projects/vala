import { getAllTickets, getReplyTicket, sendTicket } from "./api/tickets.js";
import { getDataLocal } from "./helper.js";
import { toast } from "./toastify.js";

import { successAlert } from "./Services.js";
const userId = await getDataLocal("user");

/*----------------render page------------------*/
const renderPage = async () => {
  const allTickets = await getAllTickets();
  const replyTickets = await getReplyTicket();
  const tickets = allTickets.filter((item) => item.user.id === userId);
  const container = document.querySelector("#container-tickets");

  tickets.forEach((item, index) => {
    const reply = replyTickets.filter((element) => element.ticket === item.id);
    console.log(reply);
    const note = `
        <div class="col-12 col-md-6 p-1">
        <div class="item-ticket ">
            <div class="title d-flex justify-content-between align-items-center my-2">
              <span>${item.user.name}</span>
            </div>
            <div class="des-1">
                    ${item.message}
            </div>
            <span style="color:#fff;">پاسخ ادمین</span>
            <div class="des-2">
                ${
                  !!reply.length
                    ? reply[0].message
                    : "<span class='text-warning'>درحال بررسی</span>"
                }
             </div>
          </div>
    </div>
        `;

    container.innerHTML += note;
  });
};

await renderPage();
/*----------------render page------------------*/

/*-----------------send ticket------------------*/

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

const btnSendTicket = document.querySelector("#add-ticket");

btnSendTicket.addEventListener("click", async () => {
  const text = document.querySelector("#text-ticket-add");
  if(!text.value.trim()){
    await toast("لطفا تیکت خود را وارد کید");
    text.focus()
  }

  const data = {
    message: text.value,
    user: userId,
    status: "wa",
  };

  await sendTicket(data);
  successAlert("success","تیکت شما ثبت شد ")
  setTimeout(()=>{
    location.reload()
  },3000)
});

/*-----------------send ticket------------------*/
