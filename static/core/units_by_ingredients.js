window.addEventListener("load", function() {
  (function($) {
    $("td.field-ingredient select[data-field-name='ingredient']").change(function() {
      const $this = $(this);
      const ingredient_id = $this.val();
      // todo: call this for initial values (while editing) or populate from backend.
      $.ajax({
        type: "GET",
        url: "/core/units-by-ingredient/"+ingredient_id,
        data: {},
        dataType: 'json',
        success: function(response) {
          const $unit_select = $this.closest("tr").find("td.field-unit").find("select");
          const all_options_html = [`<option value="-------"></option>`];
          $.each(response.unit_choices, function(idx, item){
            all_options_html.push(`<option value="${item[0]}">${item[1]}</option>`)
          });
          $unit_select.html(all_options_html);
        },
        error: function (response) {
          // todo: show proper error to user in an error div or using some notification engine
          console.log(response);
        }
      });
    });
  })(django.jQuery);
});
