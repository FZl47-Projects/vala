
import { baseUrl } from "../api/baseUrl.js"


const url = await baseUrl()


const urls = [
    {path : `Wedding` , color : "blue" , title : "عروسی"},
    {path : `Beauty` , color : "green" , title : "زیبایی"},
    {path : `Photographic` , color : "tree" , title : "عکاسی"},
    {path : `Medical` , color : "four" , title : "پزشکی"},
    {path : `Laboratory` , color : "five" , title : "آزمایشگاه"},
    {path : `Sports` , color : "blue" , title : "ورزشی"},
]


/*---------------render page-------------------*/

const renderPage = async() =>{

    const container = document.querySelector("#container")

    urls.forEach((item , index) => {
        const note = `<div class="col-10 col-md-8 p-2">
        <a href="./operators.html?${item.path}">
            <div class="item-profile" id="${item.color}">
                <div class="inner-item-hozori">
                    ${item.title}
                </div>
            </div>
        </a>
    </div>`


    container.innerHTML += note
    })


}


await renderPage()

/*---------------render page-------------------*/
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


