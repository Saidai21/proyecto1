$(document).ready(function(){
  $("#enviar").click(function(event){
      var valcor = true;
      var nombre = $("#itNombre").val();
      var correo = $("#itCorreo").val();
      var contrasena = $("#itContrasena").val();
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
