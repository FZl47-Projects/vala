import { getAllRavand, getAllRoutin } from "./api/routin.js";

/*---------------------render Page---------------------*/
const allRoutin = await getAllRoutin();
const ravandUser = await getAllRavand();

const renderPage = async () => {
  const container = document.querySelector("#container");

  allRoutin.forEach((item, index) => {
    const ravand = ravandUser.filter((elem) => elem.routin === item.id);

    const note = `<div class="col-12 col-md-6 p-2 kk">
        <div class="item-user">
          <!-- imge-user -->
          <div class="col-2 imge-user">
            <div>
              <img src="./assets/images/rotin/2.png" alt="">
            </div>

          </div>
          <!-- range-type -->
          <div class="col-5 contenthh" style="color: #fff;">
            <div class="name-user" >رضا آخوندی</div>
            <label id="title-type-range" for="amount-cream">روند بهبودی</label>
            <input id="amount-cream-${index}" type="range" value="0" name="cream" 
            list="amount" min="0" max='${ravand.length - 1}' step="${1}" oninput="changeHanlder(${index} , ${1})">
            <button onclick="playHandler(${1})">play</button>
            <button onclick="stopHandler()">stop</button>
          </div>
          <!-- video-rotin -->
          <div class="col-5 video-rotin">
            <div class="video-item ">
              <div class="video-item images-item" id="content-image-${index}">
                ${Object.keys(ravand)
                  .map((item) => {
                    return `
                    <img class="image-user " src="http://185.255.89.163:8000/${ravand[item].image}" alt="">
                    `;
                  })
                  .join("")}

                
              </div>
            </div>

          </div>

        </div>
      </div>`;

    container.innerHTML += note;
  });

  const images = document.querySelectorAll(".images-item")
  images.forEach(item => {
      item.children[0].classList.add("active")
  })




};

await renderPage();
/*---------------------render Page---------------------*/

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
    console.log(count);
    if (count === images.length - 1) return;
    count++;
    images.forEach((item, index) => {
      item.classList.remove("active");
    });
    images[count].classList.add("active");
    input.value += 1;
    play = true;
    console.log(play);
  }, 1000);
  window.stopHandler = () => {
    clearInterval(time);
  };
};

window.playHandler = (index, step) => {
  timer(`#content-image-${index}`, `#amount-cream-${index}`, step);
};

window.changeHanlder = (index, step) => {
  const input = document.querySelector(`#amount-cream-${index}`);

  const images = [
    ...document.querySelector(`#content-image-${index}`).children,
  ];
  const count = input.value / +step;

  if (count === images.length) return;

  images.forEach((item) => {
    item.classList.remove("active");
  });

  images[count].classList.add("active");
};
/*------------------------play and stop slider------------------------*/
