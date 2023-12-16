import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const getAllFoods = async () => {
  const res = await fetch(`${BASE_URL}food/all/`);
  const data = await res.json();
  return data;
};

const addFood = async (data) => {
  fetch(`${BASE_URL}program/food/all/`, data)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.log("error", error));

  return res.data;
};

const getAllFood = async () => {
  const res = await fetch(`${BASE_URL}program/food/all/`);

  const data = await res.json();

  return data;
};

export { addFood, getAllFoods, getAllFood };
