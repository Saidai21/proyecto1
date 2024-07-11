
// VALIDAR RUT
function validarRut(rut) {
    // Eliminar puntos y convertir a mayúsculas
    rut = rut.replace(/\./g, '').toUpperCase();

    // Verificar que el RUT contiene un guion
    if (!rut.includes('-')) {
        return false;
    }

    // Separar el número base del dígito verificador
    let partes = rut.split('-');
    let numeroBase = partes[0];
    let digitoVerificador = partes[1];

    // Validar que el formato sea correcto
    if (!numeroBase || !digitoVerificador || isNaN(numeroBase) || !/^(\d|K)$/.test(digitoVerificador)) {
        return false;
    }

    // Invertir el número base
    let numeroInvertido = numeroBase.split('').reverse().join('');

    // Multiplicar cada dígito por la secuencia 2, 3, 4, 5, 6, 7
    let suma = 0;
    let multiplicador = 2;
    for (let i = 0; i < numeroInvertido.length; i++) {
        suma += parseInt(numeroInvertido[i]) * multiplicador;
        multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
    }

    // Calcular el módulo 11
    let resto = suma % 11;
    let digitoCalculado = 11 - resto;

    // Convertir el dígito calculado
    if (digitoCalculado === 11) {
        digitoCalculado = '0';
    } else if (digitoCalculado === 10) {
        digitoCalculado = 'K';
    } else {
        digitoCalculado = digitoCalculado.toString();
    }

    // Comparar el dígito calculado con el dígito verificador
    return digitoCalculado === digitoVerificador;
}

$(document).ready(function(){
    $("#Enviar").click(function(){
        var rut = $("#RutCliente").val();
        var servicio = $("#Combobox").val();
        var fecha = $("#fecha").val();
        var problema= $("#problema").val();
        var fechaValue = new Date(fecha);
        var now=new Date();
        if (rut==""){
            $("#RutCliente").css("border-color","red")
            $("#mensajeRut2").fadeIn()
            event.preventDefault();
        }else{
            if (validarRut(rut)) {
                console.log("rut valido")
                $("#mensajeRut2").fadeOut()
                $("#mensajeRut").fadeOut()
                $("#RutCliente").css("border-color", "#ced4da")
            } else {
                console.log("rut invalido")
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
            console.log("ola")
            if(fechaValue<now){
                $("#fecha").css("border-color","red")
                $("#mensajeFecha2").fadeIn()
                event.preventDefault();
            }else{
                $("#fecha").css("border-color","#ced4da")
                $("#mensajeFecha").fadeOut()
                $("#mensajeFecha2").fadeOut()
            }
            
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