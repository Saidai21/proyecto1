// // Función para validar el RUT chileno
// function validarRut(RutCliente) {
//     if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) {
//         return false;
//     }
//     const tmp = RutCliente.split('-');
//     let digv = tmp[1];
//     const RutCliente = tmp[0];
//     if (digv == 'K') digv = 'k';
//     return (dv(RutCliente) == digv);
// }

// function dv(T) {
//     let M = 0, S = 1;
//     for (; T; T = Math.floor(T / 10)) {
//         S = (S + T % 10 * (9 - M++ % 6)) % 11;
//     }
//     return S ? S - 1 : 'k';
// }

// document.getElementById('repairForm').addEventListener('submit', function(event) {
//     const rutInput = document.getElementById('RutCliente');
//     const rutValue = rutInput.value;
//     if (!validarRut(rutValue)) {
//         rutInput.classList.add('is-invalid');
//         event.preventDefault();
//     } else {
//         rutInput.classList.remove('is-invalid');
//     }
// });



// VALIDAR RUT
function validarRUT(rut) {
    // Elimina puntos y guiones
    rut = rut.replace(/\./g, '').replace('-', '');
    
    // Verifica que tenga el formato correcto
    if (!/^[0-9]+[kK0-9]$/.test(rut)) {
        return false;
    }

    // Separa número y dígito verificador
    var cuerpo = rut.slice(0, -1);
    var dv = rut.slice(-1).toUpperCase();

    // Calcula el dígito verificador esperado
    var suma = 0;
    var multiplo = 2;

    for (var i = cuerpo.length - 1; i >= 0; i--) {
        suma += multiplo * cuerpo.charAt(i);
        multiplo = multiplo < 7 ? multiplo + 1 : 2;
    }

    var dvEsperado = 11 - (suma % 11);
    dvEsperado = dvEsperado == 11 ? '0' : dvEsperado == 10 ? 'K' : dvEsperado.toString();

    // Compara el dígito verificador ingresado con el esperado
    return dv === dvEsperado;
}

$(document).ready(function(){
    $("#Enviar").click(function(){
        var rut = $("#RutCliente").val();
        var servicio = $("#Combobox").val();
        var fecha = $("#fecha").val();
        var problema= $("#problema").val();
        if (rut==""){
            $("#RutCliente").css("border-color","red")
            $("#mensajeRut2").fadeIn()
            event.preventDefault();
        }else{
            if (validarRUT(rut)) {
                $("#mensajeRut2").fadeOut()
                $("#mensajeRut").fadeOut()
                $("#RutCliente").css("border-color", "#ced4da")
            } else {
                $("#mensajeRut2").fadeOut()
                $("#RutCliente").css("border-color","red")
                $("#mensajeRut").fadeIn()
                event.preventDefault();
            }
        }
        if(servicio==null){
            $("#Combobox").css("border-color","red")
            $("#mensajeCombo").fadeIn()
            event.preventDefault();
        }else{
            $("#Combobox").css("border-color", "#ced4da")
            $("#mensajeCombo").fadeOut()
        }

        if(fecha==""){
            $("#fecha").css("border-color","red")
            $("#mensajeFecha").fadeIn()
            event.preventDefault();
        }else{
            $("#fecha").css("border-color","#ced4da")
            $("#mensajeFecha").fadeOut()
        }
        if(problema==""){
            $("#problema").css("border-color","red")
            $("#mensajeProb").fadeIn()
            event.preventDefault();
        }else{
            $("#problema").css("border-color","#ced4da")
            $("#mensajeProb").fadeOut()
        }

        $("#RutCliente").change(function(){
            $("#RutCliente").css("border-color", "#ced4da")
            $("#mensajeRut2").fadeOut()
            $("#mensajeRut").fadeOut()
        })
        $("#Combobox").change(function(){
            $("#Combobox").css("border-color", "#ced4da")
            $("#mensajeCombo").fadeOut()
        })
        $("#fecha").change(function(){
            $("#fecha").css("border-color","#ced4da")
            $("#mensajeFecha").fadeOut()
        })
        $("#problema").change(function(){
            $("#problema").css("border-color","#ced4da")
            $("#mensajeProb").fadeOut()
        })
    })
})