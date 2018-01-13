function initMap() {
  var uluru = {lat: 43.821, lng: -79.298};
  var m = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    center: uluru
  });

  var contentString = '<div id="content">'+
  '<div id="siteNotice">'+
  '</div>'+
  '<h1 id="firstHeading" class="firstHeading">Original Noodles</h1>'+
  '<div id="bodyContent">'+
  '<p>Hi, it is me.</p>'+
  '<p>Coupon link, <a href="https://example.com?coupon=">'+
  '(last visited June 22, 2009).</p>'+
  '</div>'+
  '</div>';

  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  var image = 'bars.png';
  var marker = new google.maps.Marker({
    position: uluru,
    map: m,
    icon:image
  });

  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
}