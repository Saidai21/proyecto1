var eliminarUrl = "{% url 'eliminar_del_carrito' 0 %}";
var csrfToken = "{{ csrf_token }}";
$(document).ready(function() {
function actualizarTotal() {
    var totalPrecio = 0;
    var totalCantidad = 0;

    $('.precio').each(function() {
        var precio = $(this).text().replace('$', '');
        totalPrecio += parseFloat(precio);
    });

    $('.cantidad').each(function() {
        var cantidad = $(this).text();
        totalCantidad += parseInt(cantidad);
    });

    $('#total-precios').html('<strong>$' + totalPrecio.toFixed(2) + '</strong>');
    $('#total-cantidad').html('<strong>' + totalCantidad + '</strong>');
}

function eliminarProducto(itemId) {
    $.ajax({
        url: '{% url "eliminar_del_carrito" 0 %}'.replace('0', itemId),
        type: 'POST',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function(response) {
            if (response.success) {
                $('#item-' + itemId).remove();
                actualizarTotal();
            } else {
                alert('Error al eliminar el producto: ' + response.error);
            }
        }
    });
}

$('.eliminar-btn').on('click', function() {
    var itemId = $(this).data('id');
    eliminarProducto(itemId);
});

actualizarTotal();
});