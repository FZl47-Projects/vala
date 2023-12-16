const toast = async(text) => {
    Toastify({
        text,
        duration: 5000,
        destination: "https://github.com/apvarun/toastify-js",
        newWindow: true,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
          background: "red",
          fontSize : "24px"
        },
        onClick: function(){} // Callback after click
      }).showToast();
}


export {toast}