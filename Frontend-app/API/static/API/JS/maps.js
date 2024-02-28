function initMap() {
    var mapOptions = {
        center: new google.maps.LatLng(59.772023, 8.468946),
        zoom: 7
    };
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);

    var locations = [ // Tiltenkt at vi henter data fra databaser her for å få faktiske stasjonslokasjoner
        {lat: 59.913868, lng: 10.752245, name: "Oslo", firerisk: 4.533},
        {lat: 60.391262, lng: 5.322054, name: "Bergen", firerisk: 3.123},
        {lat: 58.964432, lng: 5.726250, name: "Stavanger", firerisk: 5.123},
        {lat: 58.1467, lng: 7.9956, name: "Kristiansand", firerisk: 4.923},
    ];

    var infowindow = new google.maps.InfoWindow();

    locations.forEach(function(location) {
        var marker = new google.maps.Marker({
            position: {lat: location.lat, lng: location.lng},
            map: map,
            title: location.name,

            icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        });

        marker.addListener('click', function() { // Tiltenkt at vi lager en API-kall mot FRCM-modulen her for å hente data om stasjonen
            infowindow.setContent('<div style="font-size: 13px;"><strong>' + location.name + '</strong><br>' +
                'Lat: ' + location.lat + '<br>Lng: ' + location.lng + '<br>FireRisk: ' + location.firerisk + '</div>');
            infowindow.open(map, marker);
        });
    });
};