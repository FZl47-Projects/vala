import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL


const analyze = async (data) => {
    const res = await fetch(`${BASE_URL}analyze/all/`, data);
    const dataF = await res.json();
    return dataF;
    
  };

  const getAllanalyze = async () => {
    const res = await axios(`${BASE_URL}analyze/all/`);
    return res.data;
  };

  export { analyze , getAllanalyze };


