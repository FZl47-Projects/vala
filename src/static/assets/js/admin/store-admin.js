// ------------------------------ Toggle delivered state handler --------------------------- //
function toggleDelivered(id, el) {
    $.get(`/shop/products/order/${id}/state/`).then(response => {
        if (response['response'] === 'ok') {
            Toast.fire({
                icon: 'success',
                title: `وضعیت ثبت شد`,
                timer: 2000,
            });
        }
    })
}
// ------------------------------ Toggle counseling state handler --------------------------- //