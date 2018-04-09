console.log("js is here....");

$(document).ready(function(){


})


$('.like').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  console.log('fix like ajax call');
  // $.ajax({
  //   url: '/like_cat/',
  //   method: "GET",
  //   data: {cat_id: element.attr('data-id')},
  //   success: function(response){
  //     element.html('Likes: ' + response);
  //   }
  // })
})
