$(document).ready(function(){
    $("#enviar").click(function(){
      var valcor= true;
      var correo=$("#itCorreo").val();
      var contrasena=$("#itContrasena").val();
      var apellido=$("#itApellido").val();
      var asunto=$("#Asunto").val();
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if(!emailRegex.test(correo)){
          $("#itCorreo").css("border-color","red");
          $("#mensajeCorreo2").fadeIn();
          valcor=false;
          return false;
          event.preventDefault(); // Evita que se envíe el formulario
      }
      if(correo==""){
        $("#itCorreo").css("border-color","red");
        $("#mensajeCorreo").fadeIn();
        return false;
      }else{
        if(valcor){
          $("#itCorreo").css("border-color","#ced4da");
          $("#mensajeCorreo").fadeOut();
        }
      }
      if(contrasena==""){
        $("#itContrasena").css("border-color","red");
        $("#mensajeContrasena").fadeIn();
        return false;
      }else{
        $("#itContrasena").css("border-color","#ced4da");
        $("#mensajeContrasena").fadeOut();
      }
    })
  })
  $("#itCorreo").change(function(){
    $("#itCorreo").css("border-color","#ced4da");
    $("#mensajeCorreo").fadeOut();
    $("#mensajeCorreo2").fadeOut();
  })
  $("#itContrasena").change(function(){
    $("#itContrasena").css("border-color","#ced4da");
    $("#mensajeContrasena").fadeOut();
  })

  $(document).ready(function(){
    $('#enviar').click(function(){
        var correo = $('#itCorreo').val();
        var contrasena = $('#itContrasena').val();
        $.ajax({
            type: 'POST',
            url: '/iniciar_sesion/',
            data: {
                correo: correo,
                contrasena: contrasena
            },
            success: function(response){
                if (response.success) {
                    $('#exampleModal').modal('show');
                } else {
                    alert('Error al iniciar sesión: ' + response.error);
                }
            },
            error: function(xhr, textStatus, errorThrown){
                alert('Error al iniciar sesión: ' + errorThrown);
            }
        });
    });
});
