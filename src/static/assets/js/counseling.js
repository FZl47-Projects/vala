
// ------------------------------ Toggle counseling state handler --------------------------- //
function answerCounseling(id, el) {
    $.get(`/operation/counseling/${id}/answer/`).then(response => {
        if (response['response'] === 'answered') {
            let state = document.querySelector('.state');

            if (el.checked) {
                state.innerHTML = 'پایان';
            } else {
                state.innerHTML = 'بی پاسخ'
            }
            state.classList.toggle('bg-danger');
            state.classList.toggle('bg-success');

            Toast.fire({
                icon: 'success',
                title: `وضعیت ثبت شد`,
                timer: 2000,
            })
        }
    })
}
// ------------------------------ Toggle counseling state handler --------------------------- //
