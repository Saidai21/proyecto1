$(document).ready(function(){
  $("#enviar").click(function(event){
      var valcor = true;
      var correo = $("#correo").val();
      var contrasena = $("#contrasena").val();
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      // Validar correo
      if (!emailRegex.test(correo)){
          $("#correo").css("border-color","red");
          $("#mensajeCorreo2").fadeIn();
          valcor = false;
          event.preventDefault(); 
      } else {
          if (correo == ""){
              $("#correo").css("border-color","red");
              $("#mensajeCorreo").fadeIn();
              event.preventDefault();
          } else {
              if (valcor){
                  $("#correo").css("border-color","#ced4da");
                  $("#mensajeCorreo").fadeOut();
                  $("#mensajeCorreo2").fadeOut();
              }
          }
      }

      // Validar contraseña
      if (contrasena == ""){
          $("#contrasena").css("border-color","red");
          $("#mensajeContrasena").fadeIn();
          event.preventDefault();
      } else {
          $("#contrasena").css("border-color","#ced4da");
          $("#mensajeContrasena").fadeOut();
      }
  });

  // Limpiar mensajes de error al cambiar el valor del correo
  $("#correo").change(function(){ 
      $("#correo").css("border-color","#ced4da");
      $("#mensajeCorreo").fadeOut();
      $("#mensajeCorreo2").fadeOut();
  });

  // Limpiar mensajes de error al cambiar el valor de la contraseña
  $("#contrasena").change(function(){
      $("#contrasena").css("border-color","#ced4da");
      $("#mensajeContrasena").fadeOut();
  });
});
