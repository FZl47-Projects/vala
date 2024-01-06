// ---------------------------- Add data to request modal -------------------------- //
$('#requestProductModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget);
    let primaryKey = button.data('primarykey');
    let productTitle = button.data('product-title')

    console.log(primaryKey, productTitle);

    let modal = $(this);
    modal.find('.modal-body #ProductId').val(primaryKey);
    modal.find('.modal-body #productTitle').text(productTitle);
})
// ------------------------- Add data to request  modal -------------------------- //
