console.log("js is here....");

$(document).ready(function(){

  $('select').formSelect();
  // $('main.scrollspy').scrollSpy();
})


$('.like').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_product/',
    method: "GET",
    data: {product_id: element.attr('data-id')},
    success: function(response){
      element.html('Likes: ' + response);
    }
  })
})

// $('.edit_product').on('click', function(event){
//   event.preventDefault();
//   var element = $(this);
//   $.ajax({
//     url: '/like_product/',
//     method: "GET",
//     data: {product_id: element.attr('data-id')},
//     success: function(response){
//       element.html('Likes: ' + response);
//     }
//   })
// })
