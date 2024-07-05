$(document).ready(function(){
    $("#enviar").click(function(event){
      var valcor= true;
      var correo=$("#correo").val();
      var contrasena=$("#contrasena").val();
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if(!emailRegex.test(correo)){
          $("#correo").css("border-color","red");
          $("#mensajeCorreo2").fadeIn();
          valcor=false;
          event.preventDefault(); 
      }else{
        if(correo==""){
          $("#correo").css("border-color","red");
          $("#mensajeCorreo").fadeIn();
          event.preventDefault();
        }else{
          if(valcor){
            $("#correo").css("border-color","#ced4da");
            $("#mensajeCorreo").fadeOut();
          }
        }
      }

      if(contrasena==""){
        $("#contrasena").css("border-color","red");
        $("#mensajeContrasena").fadeIn();
        event.preventDefault();
      }else{
        $("#contrasena").css("border-color","#ced4da");
        $("#mensajeContrasena").fadeOut();
      }
    })
  })
  $("#correo").change(function(){
    $("#correo").css("border-color","#ced4da");
    $("#mensajeCorreo").fadeOut();
    $("#mensajeCorreo2").fadeOut();
  })
  $("#contrasena").change(function(){
    $("#itContrasena").css("border-color","#ced4da");
    $("#mensajeContrasena").fadeOut();
  })