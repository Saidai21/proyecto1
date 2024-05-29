// Función para validar el RUT chileno
function validarRut(RutCliente) {
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) {
        return false;
    }
    const tmp = RutCliente.split('-');
    let digv = tmp[1];
    const RutCliente = tmp[0];
    if (digv == 'K') digv = 'k';
    return (dv(RutCliente) == digv);
}

function dv(T) {
    let M = 0, S = 1;
    for (; T; T = Math.floor(T / 10)) {
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    }
    return S ? S - 1 : 'k';
}

document.getElementById('repairForm').addEventListener('submit', function(event) {
    const rutInput = document.getElementById('RutCliente');
    const rutValue = rutInput.value;
    if (!validarRut(rutValue)) {
        rutInput.classList.add('is-invalid');
        event.preventDefault();
    } else {
        rutInput.classList.remove('is-invalid');
    }
});