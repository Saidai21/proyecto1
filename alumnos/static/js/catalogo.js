
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
      $(document).ready(function() {
        $('#showAllBikes').click(function() {
            $('.collapse').collapse('show');
        });
    });
      
