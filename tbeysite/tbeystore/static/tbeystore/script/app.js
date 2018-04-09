console.log("js is here....");
var elem = document.querySelector('select');
// var instance = M.FormSelect.init(elem, options);

$(document).ready(function(){

  // $('select').material_select();
  $('select').formSelect();
})


$('.like').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  // console.log('fix like ajax call');
  // console.log(element);
  $.ajax({
    url: '/like_product/',
    method: "GET",
    data: {product_id: element.attr('data-id')},
    success: function(response){
      element.html('Likes: ' + response);
    }
  })
})
