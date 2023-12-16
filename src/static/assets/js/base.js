// URLS
const BASE_URL = 'http://localhost/projects/vala/frontend'
const LOGIN_URL = _getURL('login.html')
const HOME_URL = _getURL('index.html')
const OPERATOR_INDEX_URL = _getURL('Operator/index.html')


function _getURL(url){
    return `${BASE_URL}/${url}`
}


function redirect(url) {
    window.location.href = url
}


function createNotFound(container){
    removeNotFound(container)
    let not_found = document.createElement('div')
    not_found.classList.add('container-not-found-base')
    not_found.innerHTML = getElementNotFound()
    container.appendChild(not_found)
}

function removeNotFound(container){
    try{
        container.querySelector('.container-not-found-base').remove()
    }catch(e){}
}

function getElementNotFound(){
    return `
        <div>
            <p>چیزی یافت نشد</p>
        </div>
    `
}

function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;
    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

function randomString(length=15) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}

