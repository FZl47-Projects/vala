const BASE_API_URL = 'http://127.0.0.1:8001/'


function error_status_handler(status){
    if (status == 401){
        redirect(LOGIN_URL)
    }else if (status == 403){
        createNotify({
            title: 'ارور',
            message: 'شما دسترسی ندارید',
            closeOnClick: true,
            positionClass: 'nfc-top-right',
            showDuration: 5000,
            theme: 'error'
        })
    }
}

function callApi(url, {
    data = {}, auth = true, auth_redirect = true, response = () => {
    }, error = null, method = 'post', loading_el = null, loading_size = 'small', loading_color = '#39ff8c',loading_fill=null
}) {

    // Use AJAX instead fetch (for now)

    function creat_loading() {
        if (loading_el) {
            createLoading(loading_el, {
                'size': loading_size,
                'color': loading_color,
                'fill':loading_fill
            })
        }

    }

    function remove_loading() {
        if (loading_el) {
            removeLoading(loading_el)
        }
    }

    headers = {
        'content-type': 'application/json',
    }
    

    if (auth) {
        token = getCookie('token')
        if (!token) {
            // redirect to login page
            if (auth_redirect) {
                redirect(LOGIN_URL)
            }
        }
        headers['Authorization'] = `Token ${token}`
    }

    if (!error) {
        error = function () {
            createNotify({
                title: 'ارور',
                message: 'مشکلی در درخواست به سرور وجود دارد لطفا از اتصال خود اطمینان پیدا کنید',
                showDuration: 7000,
                theme: 'error'
            })
        }
    }

    creat_loading()
    $.ajax({
        url: url,
        data: JSON.stringify(data),
        type: method,
        timeout: 1000 * 60, // 1 min
        success: function (rspns) {
            remove_loading()
            response(rspns)
        },
        headers: headers,
        error: function (response) {
            error_status_handler(response.status)
            remove_loading()
            error(response)

        },
        fail: function (response) {
            error_status_handler(response.status)
            remove_loading()
            error(response)
        },
    })


    // fetch(url, {
    //     'method': method,
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'Accept': 'application/json',
    //         // 'Access-Control-Allow-Origin': '*',
    //     },
    //     'body': data
    // }).then((response) => {
    //     if (response.ok) {
    //         return response.json();
    //     } else {
    //         return response.text().then(text => { throw new Error(text) })
    //     }
    // })
    //     .then((responseJson) => {
    //         response(responseJson)
    //     })
    //     .catch((error) => {
    //         console.log(error)
    //     });

}


function createLoading(element, options) {
    if (element.classList.contains('loading-element-parent')) {
        return
    }
    let loading = document.createElement('div')
    loading.className = `loading-element loading-circle-${options.size}`
    let color = options.color || '#1ee696'
    loading.style = `
        border-top-color:${color};
        border-right-color:${color};
    `
    let loading_blur = document.createElement('div')
    if (options.fill){
        loading_blur.style = `
            background:${options.fill};
        `
        loading_blur.classList.add('fill')
    }
    loading_blur.className = 'loading-blur-element'
    element.append(loading_blur)
    element.append(loading)
    element.classList.add('loading-element-parent')
    element.setAttribute('disabled', 'disabled')
}

function removeLoading(element) {
    try {
        element.querySelector('.loading-element').remove()
        element.querySelector('.loading-blur-element').remove()
        element.classList.remove('loading-element-parent')
        element.removeAttribute('disabled')
    } catch (e) {

    }
}


function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function removeCookie(name) {
    document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}


// export {callApi,setCookie,getCookie,removeCookie,redirect,createLoading,BASE_API_URL}