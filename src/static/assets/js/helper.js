const shortTicket = (text, count) => {
  const data = text.split("");
  const dataOne = data.slice(0, count);
  const result = dataOne.join("");

  return result;
};

const getId = (text) => {
  const data = text.split("");
  const dataOne = data.slice(1);
  const result = dataOne.join("");
  return result;
};
const getPath = (text) => {
  const data = text.split("");
  const dataOne = data.slice(1);
  const result = dataOne.join("");
  return result;
};

const removeUserLocal = async (name) => {
  window.localStorage.removeItem(name);
};
const setUserLocal = async (name, id) => {
  window.localStorage.setItem(name, JSON.stringify(id));
};

const getUserLocalStorage = async (name) => {
  const id = JSON.parse(window.localStorage.getItem(name));
  return id;
};

const getDataLocal =async(name) => {
  const result = JSON.parse(window.localStorage.getItem(name))
  return result
}

const setDataToLocal = async (name, data) => {
  window.localStorage.setItem(name , JSON.stringify(data))


};



const phoneHandler = (text) => {
  console.log(text);
  const one = text.split("")
  const two = one.slice(1)
  const three = `+98${two.join("")}`

  return three;
}
const phoneHandlerReverse = (text) => {
  console.log(text);
  const one = text.split("")
  const two = one.slice(3)
  const three = `0${two.join("")}`

  return three;
}





export {
  shortTicket,
  phoneHandlerReverse,
  getId,
  removeUserLocal,
  setUserLocal,
  getUserLocalStorage,
  setDataToLocal,
  getDataLocal,
  getPath,
  phoneHandler
};
