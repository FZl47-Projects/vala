import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const getAllPost = async () => {
  const res = await axios(`${BASE_URL}post/all/`);
  return res.data;
};
const getPostWithOp = async (id) => {
  const res = await axios(`${BASE_URL}post/GetId/?id=${id}`);
  return res.data;
};
const addPost = async (data) => {
  console.log(data);
  const res = await fetch(`${BASE_URL}post/all/`, data);
  const dataF = await res.json();
 
  return dataF;
  
};

const likePost = async (id, data) => {
  const res = await fetch(`${BASE_URL}post/GetId/${id}/`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const dataF = await res.json();


  return dataF;
};

const editPost = async (data, id) => {
  const res = await fetch(`${BASE_URL}post/GetId/${id}/`, data);
  const dataF = await res.json();
  console.log(dataF)
  return dataF;
};

const deletePost = async (id, data) => {
  const res = await fetch(`${BASE_URL}post/GetId/${id}/`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  });
  const dataF = await res.json();
  
  return dataF;
};
const onDeletePost = async (id, data) => {
  const res = await fetch(`${BASE_URL}post/GetId/${id}/`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  });
  const dataF = await res.json();
  
  return dataF;
};
export { getAllPost, addPost, likePost, editPost,deletePost,onDeletePost,getPostWithOp };
