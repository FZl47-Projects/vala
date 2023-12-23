function redirect(url) {
    window.location.href = url
}

function sendAjax({url, data, method = 'post', success, error}) {

    success = success || function (response) {
    }
    error = error || function (response) {
        createNotify(
            {
                title: 'ارور',
                message: 'مشکلی در ارسال درخواست وجود دارد لطفا اتصال خود را بررسی کنید',
                theme: 'error'
            }
        )
    }

    $.ajax(
        {
            url: url,
            data: JSON.stringify(data),
            type: method,
            headers: {
                'X-CSRFToken': window.CSRF_TOKEN
            },
            success: function (response) {
                success(response)
            },
            failed: function (response) {
                error(response)
            },
            error: function (response) {
                error(response)
            }
        }
    )
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
}

function randomString(length = 15) {
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


function createLoading(element, options = {
    size: 'normal',
    color: '#1ee696',
    fill: null

}) {
    if (element.classList.contains('loading-element-parent')) {
        return
    }
    let loading = document.createElement('div')
    loading.className = `loading-element loading-circle-${options.size}`
    let color = options.color
    loading.style = `
        border-top-color:${color};
        border-right-color:${color};
    `
    let loading_blur = document.createElement('div')
    if (options.fill) {
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


let all_datetime_convert = document.querySelectorAll('.datetime-convert')
let all_datetime_convert_inputs = document.querySelectorAll('.datetime-convert-inp')

for (let dt_el of all_datetime_convert) {
    let dt = dt_el.innerHTML
    dt_el.setAttribute('datetime', dt)
    let dt_persian = new Date(dt).toLocaleDateString('fa-IR', {
        hour: '2-digit',
        minute: '2-digit'
    });
    if (dt_persian != 'Invalid Date') {
        dt_el.innerHTML = dt_persian
    }
}

for (let dt_el of all_datetime_convert_inputs) {
    let dt = dt_el.value
    dt_el.setAttribute('datetime', dt)
    let dt_persian = new Date(dt).toLocaleDateString('fa-IR', {
        hour: '2-digit',
        minute: '2-digit'
    });
    if (dt_persian != 'Invalid Date') {
        dt_el.value = dt_persian
    }
}


// price elements
document.querySelectorAll('.price-el').forEach((el) => {
    let p = el.innerText
    el.setAttribute('price-val', p)
    el.innerHTML = numberWithCommas(p)
})

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}


// full size element
document.querySelectorAll('.click-full-size').forEach(function (el) {
    el.addEventListener('click', function () {
        this.requestFullscreen()
    })
})


function secToDateTime(secs) {
    var t = new Date(1970, 0, 1);
    t.setSeconds(secs);
    return t;
}

function getFormattedDate(date) {
    let str = date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate() + " " + date.getHours() + ":" + date.getMinutes()
    return str
}

function getRawPhonenumber(phonenumber) {
    return String(phonenumber).replace('+98', '')
}

function truncate(str, max) {
    return str.length > max ? str.substr(0, max - 1) + '…' : str;
}


// features update
document.querySelectorAll('.features-update').forEach(function (el) {
    let feature_dis = document.createElement('div')
    feature_dis.classList.add('features-update-disable-el')
    if (el.classList.contains('features-update-parent')) {
        el.parentElement.appendChild(feature_dis)
    } else {
        el.appendChild(feature_dis)
    }


    feature_dis.addEventListener('click', function (e) {
        createNotify({
            title: '',
            message: 'بخش مورد نظر در اپدیت های بعدی اضافه میشود',
            theme: 'warning',
            showDuration: 7000
        })
    })
})

// add query params to href
let query_params = (new URL(location)).searchParams;
document.querySelectorAll('.add-params-to-href').forEach(function (el) {
    let href = el.getAttribute('href')
    let href_params = new URLSearchParams(href)
    for (let p of query_params) {
        if (!p in href) {
            href_params.set(p[0], p[1])
        }
    }
    let params = href_params.toString()
    if (params.indexOf('?') == -1) {
        params = '?' + params
    }
    el.setAttribute('href', params)
})

// validate hidden field in form
document.querySelectorAll('.form-with-hidden-field').forEach(function (form) {

    form.addEventListener('submit', function (e) {
        let valid = true
        let hidden_fields = form.querySelectorAll('input[type="hidden"][required]')
        for (let field of hidden_fields) {
            if (!field.value) {
                field.parentElement.classList.add('input-group-invalid')
                valid = false
            }
        }
        if (!valid) {
            e.preventDefault()
        }
    })
})