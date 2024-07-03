
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
      
    $(document).ready(function() {
      // Función para obtener las tasas de cambio y actualizar los precios
      function updatePrices(currency) {
          $.ajax({
              url: "https://api.exchangerate-api.com/v4/latest/CLP",
              success: function(response) {
                  var rates = response.rates;
                  var baseRate = rates[currency];
                  $('.precio').each(function() {
                      var basePrice = $(this).data('precio');
                      var newPrice = basePrice * baseRate;
                      $(this).text('$ ' + newPrice.toFixed(2) + ' ' + currency);
                  });
              },
              error: function() {
                  alert('Error al obtener las tasas de cambio.');
              }
          });
      }

      // Evento de cambio de moneda
      $('#moneda').change(function() {
          var selectedCurrency = $(this).val();
          updatePrices(selectedCurrency);
      });

      // Actualizar precios al cargar la página con la moneda por defecto
      updatePrices($('#moneda').val());
  });