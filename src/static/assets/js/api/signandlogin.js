import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const login = async (phone,password) => {
  const res = await fetch(`${BASE_URL}user/Login/?password=${password}&&phone=${phone}/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const dataF = await res.json();

  return dataF;
};



const addUser = async (data ) => {
  const res = await fetch(`${BASE_URL}user/all/` , data);
  const dataF = await res.json();
  console.log(dataF)
  return dataF;
};

export { login , addUser };
