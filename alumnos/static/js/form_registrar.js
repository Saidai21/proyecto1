$(document).ready(function(){
  $("#enviar").click(function(event){
      var valcor = true;
      var nombre = $("#itNombre").val();
      var correo = $("#itCorreo").val();
      var contrasena = $("#itContrasena").val();
      var contrasena2 = $("#itContrasena2").val();
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      
      if(!emailRegex.test(correo)){
          $("#itCorreo").css("border-color", "red");
          $("#mensajeCorreo2").fadeIn();
          valcor = false;
          event.preventDefault();
      }else{
        if(correo == ""){
            $("#itCorreo").css("border-color", "red");
            $("#mensajeCorreo").fadeIn();
            valcor = false;
            event.preventDefault();
        } else if(valcor) {
            $("#itCorreo").css("border-color", "#ced4da");
            $("#mensajeCorreo").fadeOut();
            $("#mensajeCorreo2").fadeOut();
        }
      }
      


      if(nombre == ""){
          $("#itNombre").css("border-color", "red");
          $("#mensajeNombre").fadeIn();
          valcor = false;
          event.preventDefault();
      } else {
          $("#itNombre").css("border-color", "#ced4da");
          $("#mensajeNombre").fadeOut();
      }

      if(contrasena == ""){
          $("#itContrasena").css("border-color", "red");
          $("#mensajeContrasena").fadeIn();
          valcor = false;
          event.preventDefault();
      } else {
          $("#itContrasena").css("border-color", "#ced4da");
          $("#mensajeContrasena").fadeOut();
      }

      if(contrasena2!=""){
        if(contrasena2 != contrasena){
            $("#itContrasena2").css("border-color", "red");
            $("#mensajeContrasena2").fadeIn();
            $("#mensajeContrasena3").fadeOut();
            valcor = false;
            event.preventDefault();
        } else {
            $("#itContrasena2").css("border-color", "#ced4da");
            $("#mensajeContrasena2").fadeOut();
            $("#mensajeContrasena3").fadeOut();
        }
      }else if(contrasena2 == ""){
        $("#itContrasena2").css("border-color", "red");
        $("#mensajeContrasena3").fadeIn();
        event.preventDefault();
      }else{
        $("#itContrasena2").css("border-color", "#ced4da");
        $("#mensajeContrasena3").fadeOut();
      }

      if (!valcor) {
          event.preventDefault(); // Evita que se envíe el formulario si hay errores de validación
      }else{
        $("#mensajeSuccess").fadeIn()
      }
  });

  $("#itCorreo").change(function(){
      $("#itCorreo").css("border-color", "#ced4da");
      $("#mensajeCorreo").fadeOut();
      $("#mensajeCorreo2").fadeOut();
  });
  $("#itContrasena").change(function(){
      $("#itContrasena").css("border-color", "#ced4da");
      $("#mensajeContrasena").fadeOut();
  });
  $("#itNombre").change(function(){
      $("#itNombre").css("border-color", "#ced4da");
      $("#mensajeNombre").fadeOut();
  });


});
