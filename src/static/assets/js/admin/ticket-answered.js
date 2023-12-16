import{getReplyWithOpId} from "../api/tickets.js"


const renderpage = async ()=>{
  const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id  = urlParams.get('id')
  const tickets = await getReplyWithOpId(id);
  tickets.forEach(item=>{
    console.log(item);
    const note = `  <div class="col-12 col-md-6 p-2">
    <div class="ticket-item">
      <div class="col-4 col-md-3 d-flex d-flex flex-column align-items-center justify-content-center">
        <div class="imge-user">
          <img src="http://185.255.89.163:8000${item.ticket.user.profileimage}" alt="">
        </div>

      </div>
      <div class="col-5 col-md-6 content-ticket">
        <div class="name-user">${item.ticket.user.name}</div>
        <div class="description">
          <div>${item.ticket.message}</div>
          <div class="more" id="more-btn"> در ادامه...</div>


        </div>


      </div>
      <div class="col-3 col-md-3 btn-answer-ticket">
        
        <span class='btn-answer btn-modal-1' id="btn_ans_op"> پاسخ اپراتور</span>"
        

      </div>

    </div>

 </div>`
 const op = `
 
 <div class="content-modal answer-op">
 <div class="inner-modal">
   <form class="px-4 pt-2">
     <div class="py-2">
       <div class="content-more-ticket">
    ${item.message}
       </div>

     </div>
   </form>
 </div>
</div>
`
const more = `
<div class="content-modal more-ticket">
<div class="inner-modal">
  <form class="px-4 pt-2">
    <div class="py-2">
      <div class="content-more-ticket">
      ${item.ticket.message}
      </div>

    </div>
  </form>
</div>
</div>
`
document.querySelector("#row").innerHTML+=note
document.querySelector("#modal").innerHTML +=op
document.querySelector("#modal").innerHTML +=more
  })
}
await renderpage()

const btn_more = document.querySelectorAll("#more-btn");
console.log(btn_more);
const modal_more_tickets = document.querySelectorAll(".more-ticket");
btn_more.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_more_tickets[index].classList.add("active");
      });
     
    });
    modal_more_tickets.forEach((item, index) => {
        item.addEventListener("click", (e) => {
          if (e.target.className === "inner-modal")
          modal_more_tickets[index].classList.remove("active");
        });
      });

const btn_ans_op = document.querySelectorAll("#btn_ans_op");
const modal_ans_op = document.querySelectorAll(".answer-op");
btn_ans_op.forEach((item, index) => {
    item.addEventListener("click", () => {
        modal_ans_op[index].classList.add("active");
      });
     
    });
    modal_ans_op.forEach((item, index) => {
        item.addEventListener("click", (e) => {
          if (e.target.className === "inner-modal")
          modal_ans_op[index].classList.remove("active");
        });
      });
