import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const addProduct = async (data) => {
    const res = await fetch(`${BASE_URL}store/product/all/`, data);
    const dataF = await res.json();
   
    return dataF;
    
  };

  const getAllProduct = async () => {
    const res = await axios(`${BASE_URL}store/product/all/`);
    return res.data;
  };
  const InsertOrder = async (data) => {
    const res = await axios.post(`${BASE_URL}store/all/`,data);
    return res.data;
  };
  export { addProduct , getAllProduct ,InsertOrder};
  