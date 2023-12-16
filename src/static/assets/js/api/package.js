import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL




const createPackage = async() => {

    const res = await fetch(`${BASE_URL}package/all/`)


}


export {createPackage}