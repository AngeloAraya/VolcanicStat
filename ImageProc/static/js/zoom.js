jQuery(function($){

  $('#jcrop_target').Jcrop({
    onChange:   showCoords,
    onSelect:   showCoords
  });

});

function showCoords(c)
{
  alert('x='+ c.x +' y='+ c.y +' x2='+ c.x2 +' y2='+ c.y2)
  alert('w='+c.w +' h='+ c.h)
};