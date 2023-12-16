import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const getAllRoutin = async () => {
  const res = await fetch(`${BASE_API_URL}routin/all/`);
  const data = await res.json();

  return data;
};

const getAllRoutinwithuser= async (id) => {
  const res = await fetch(`${BASE_API_URL}routin/GetId/?id=${id}`);
  const data = await res.json();

  return data;
};
const getAllRavand = async() =>{
    const res = await fetch(`${BASE_API_URL}ravand/all/`)
    const  data = await res.json()


    return data
}
const getAllRavandWithUser = async(id) =>{
  const res = await fetch(`${BASE_API_URL}ravand/GetId/?id=${id}`)
  const  data = await res.json()


  return data
}
const getAllImageRavandWithUser = async(id) =>{
  const res = await fetch(`${BASE_API_URL}ravand/image/GetId/${id}/`)
  const  data = await res.json()


  return data
}


const addRoutin = async (data) => {
  const res = await fetch(`${BASE_API_URL}routin/all/`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const dataF = await res.json();

  return dataF;
};

const addRavand = async (data) => {
  const res = await axios.post(`${BASE_API_URL}ravand/all/`, data);
  
  return res.data;
};
const addImageRavand = async (data) => {
  const res = await fetch(`${BASE_API_URL}ravand/image/all/`, data);
  const dataF = await res.json();
    console.log(dataF)
  return dataF;
};

export { getAllRoutin, addRoutin ,addRavand , getAllRavand,getAllRavandWithUser,getAllImageRavandWithUser,addImageRavand,getAllRoutinwithuser};
