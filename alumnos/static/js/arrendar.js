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
        }else{
            $("#mensajeNombre").fadeOut()
            $("#nombreCliente").css("border-color", "#ced4da")
        }
        if(periodoArriendo==""){
            $("#mensajePeriodo").fadeIn();
            $("#periodoArriendo").css("border-color","red")
            event.preventDefault();
        }else{
            if(periodoArriendo<=0){
                $("#mensajePeriodo2").fadeIn();
                $("#periodoArriendo").css("border-color","red")
                event.preventDefault();
            }else{
                $("#mensajePeriodo2").fadeOut();
                $("#mensajePeriodo").fadeOut()
                $("#periodoArriendo").css("border-color", "#ced4da")
            }
        }
        if(formaPago==null){
            $("#mensajeForma").fadeIn();
            $("#formaPago").css("border-color","red")
            event.preventDefault();
        }else{
            $("#mensajeForma").fadeOut();
            $("#formaPago").css("border-color", "#ced4da")
        }
        if(depositoGarantia==""){
            $("#mensajeDeposito").fadeIn();
            $("#depositoGarantia").css("border-color","red")
            event.preventDefault();
        }else{
            if(depositoGarantia<=0){
                $("#mensajeDeposito2").fadeIn();
                $("#depositoGarantia").css("border-color","red")
                event.preventDefault();
            }else{
                $("#mensajeDeposito2").fadeOut();
                $("#mensajeDeposito").fadeOut()
                $("#depositoGarantia").css("border-color", "#ced4da")
            }
        }
        $("#nombreCliente").change(function(){
            $("#nombreCliente").css("border-color", "#ced4da")
            $("#mensajeNombre").fadeOut()
        })
        $("#periodoArriendo").change(function(){
            $("#mensajePeriodo2").fadeOut();
            $("#mensajePeriodo").fadeOut()
            $("#periodoArriendo").css("border-color", "#ced4da")
        })
        $("#formaPago").change(function(){
            $("#mensajeForma").fadeOut();
            $("#formaPago").css("border-color", "#ced4da")
        })
        $("#depositoGarantia").change(function(){
            $("#mensajeDeposito2").fadeOut();
            $("#mensajeDeposito").fadeOut()
            $("#depositoGarantia").css("border-color", "#ced4da")
        })
    })
})