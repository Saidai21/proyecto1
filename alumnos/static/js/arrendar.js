$(document).ready(function(){
    $("#Enviar").click(function(){
        var nombreCliente=$("#nombreCliente").val();
        var periodoArriendo=$("#periodoArriendo").val();
        var formaPago=$("#formaPago").val();
        var depositoGarantia=$("#depositoGarantia").val();
        if (nombreCliente==""){
            $("#mensajeNombre").fadeIn()
            $("#nombreCliente").css("border-color","red")
            event.preventDefault();
        }

    })
})