import {BASE_API_URL} from '../api/baseUrl.js'
const BASE_URL = BASE_API_URL

const addProgram = async (data) => {

    const res = await fetch(`${BASE_URL}program/program/all/` , {
        method :"POST",
        body :JSON.stringify(data),
        headers : {
            "Content-Type" : "application/json"
        }
    })

    const dataF = await res.json()

    console.log(dataF)

    return dataF

};

export { addProgram };
