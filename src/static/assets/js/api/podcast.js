import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const addPodcast = async (data) => {
  const res = await fetch(`${BASE_URL}post/all/`, data);
  const dataF = await res.json();
  console.log(dataF);
  return dataF;
};
const GetPodcast = async () => {
  const res = await fetch(`${BASE_URL}post/category/all/`);
  const dataF = await res.json();
  console.log(dataF);
  return dataF;
};
const InsertPodcast = async (data) => {
  const res = await fetch(`${BASE_URL}post/category/all/`,data);
  const dataF = await res.json();
  console.log(dataF);
  return dataF;
};
export { addPodcast ,GetPodcast,InsertPodcast};
