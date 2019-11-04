function initMap() {
  var center = {lat: 43.980196, lng: -120.852188};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: center
  });

  var infowindow =  new google.maps.InfoWindow({});
    var marker, count;
    for (count = 0; count < data.length; count++) {
        var location = data[count]["location"]
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(location["lat"], location["lng"]),
          map: map,
          title: data[count]["name"]
        });
    google.maps.event.addListener(marker, 'click', (function (marker, count) {
          return function () {
            infowindow.setContent(`[${data[count]["rating"]} (${data[count]["num_reviews"]})] ${data[count]["name"]}`);
            // infowindow.setContent(data[count]["name"] + " " + data[count]["rating"]);
            infowindow.open(map, marker);
          }
        })(marker, count));
      }

}