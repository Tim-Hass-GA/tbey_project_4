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

// $('.add_to_order').on('click', function(event){
//   event.preventDefault();
//   var element = $(this);
//   console.log('add_to_order click');
//   console.log(element.attr('data-id'))
//   $.ajax({
//     url: '/add_to_order/',
//     method: "GET",
//     data: {product_id: element.attr('data-id')},
//     success: function(response){
//       // element.html('Items Left: ' + response);
//       console.log('success')
//     }
//   })
// })
