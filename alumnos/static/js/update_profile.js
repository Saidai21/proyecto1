$(document).ready(function(){
    $("#Actualizar").click(function(event){
        var correo=$("#id_correo").val();
        var valcor=true
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        console.log(correo)
        if(!emailRegex.test(correo)){
            $("#itCorreo").css("border-color", "red");
            $("#mensajeCorreo2").fadeIn();
            valcor = false;
            event.preventDefault();
        }else{
        if(correo == ""){
            $("#itcorreo").css("border-color", "red");
            $("#mensajeCorreo").fadeIn();
            valcor = false;
            event.preventDefault();
        } else if(valcor) {
            $("#itcorreo").css("border-color", "#ced4da");
            $("#mensajeCorreo").fadeOut();
        }
        }

    })
})