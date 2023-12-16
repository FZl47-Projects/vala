import { getAllFood, getProgram } from "../api/managers.js";
import { addProgram } from "../api/program.js";
import { getDataLocal, getPath } from "../helper.js";
import { validateLogin } from "../api/validateLoginAdmin.js";
await validateLogin()
const userId = await getPath(window.location.search);

const opraotrId = await getDataLocal("user-admin");

const table = [
  { title: "شنبه" },
  { title: "یکشنبه" },
  { title: "دو شنبه" },
  { title: "سه شنبه" },
  { title: "چهار شنبه" },
  { title: "پنح شنبه" },
  { title: "جمعه" },
];
const v = [
  { v: "صبجانه" },
  { v: "میان وعده" },
  { v: "ناهار " },
  { v: "میان وعده" },
  { v: "شام" },
];

/*--------------------render Page---------------------*/

const renderPage = async () => {
  const container = document.querySelector("#content");
  const containerHafteh = document.querySelector("#hafteh");
  const containerVaedeh = document.querySelector("#vaedeh");

  table.forEach(async (item, index) => {
    const getFood = await getAllFood(opraotrId);
    const note = `
    <div class="text-center" style="width : 12.5%">${item.title}</div>
    `;
    const noteOne = `<div class="d-flex justify-content-between align-items-center flex-column text-center  nn" style="width : 12.5%">
    ${Object.keys(v)
      .map((key) => {
        return `
            <select>
            ${Object.keys(getFood)
              .map((key) => {
                return `
                <option value=${getFood[key].id}>${getFood[key].name}</option>
                  `;
              })
              .join("")}
            </select>
          `;
      })
      .join("")}
  </div>`;
    containerHafteh.innerHTML += note;
    container.innerHTML += noteOne;
  });




  
  //     const getFood = await getAllFood(opraotrId);

  //     const noteOne = `<tr>

  //     ${Object.keys(v)
  //       .map((key) => {
  //         return `
  //         <td class="name-food d-flex flex-column ">${v[key].v}</td>
  //       `;
  //       })
  //       .join("")}
  //     ${Object.keys(table)
  //       .map((key) => {
  //         return `
  //           <td><span><select name="brand" id="noe-moshavereh"
  //      class="name">
  //      ${Object.keys(getFood)
  //        .map((key) => {
  //          return `
  //           <option value=${getFood[key].id}>${getFood[key].name}</option>

  //           `;
  //        })
  //        .join("")}
  //     </select></span></td>
  //           `;
  //       })
  //       .join("")}

  //     </tr>
  //     `;

  //     container.innerHTML += noteOne;
  //   });
};

await renderPage();

/*--------------------render Page---------------------*/

const btnAddTableFood = document.querySelector("#sabt");




btnAddTableFood.addEventListener("click", async () => {
    const data = {
      user: userId,
      oprator: opraotrId,
      types: "Food",
    };

    const ttt = await addProgram(data);
    

//   const selects = [...document.querySelectorAll("select")];

//   let i = 0;

//   for (let i = 0; i < selects.length; i++) {
//     console.log(selects[i]);
//   }
});


console.log(await getProgram(userId))