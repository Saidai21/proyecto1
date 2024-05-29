
      $(document).ready(function(){
        $('.btn').click(function(){
          const target = $(this).data('target');
          const allCollapse = $('.collapse');

          allCollapse.each(function(){
            if($(this).attr('id') !== target){
              $(this).removeClass('show');
              const buttonControlled = $(`[data-target="#${$(this).attr('id')}"]`);
              buttonControlled.attr('aria-expanded', 'false');
            }
            
          });
        });
      });
      $(document).ready(function(){
        // Función para manejar el evento click del botón "Mostrar todas las bicicletas"
        $('#showAllBikes').click(function () {
          $('.collapse').collapse('show');
        });
      });
      
