import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const getAllChat = async () => {
  const res = await fetch(`${BASE_URL}chat/all/`);
  const data = await res.json();

  return data;
};

const addChat = async (data) => {
  const res = await fetch(`${BASE_URL}chat/all/`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const dataF = await res.json();

  console.log(dataF);
  return dataF;
};

export { addChat, getAllChat };
