import React, { useEffect, useRef } from "react";
import "./GoogleMaps.css";

const GoogleMaps = () => {
  const googleMapRef = useRef(null);
  const googleMap = useRef(null);

  useEffect(() => {
    var markersData = [
      { lat: 59.913868, lng: 10.752245, name: "Oslo", firerisk: 4.533 },
      { lat: 60.391262, lng: 5.322054, name: "Bergen", firerisk: 3.123 },
      { lat: 58.964432, lng: 5.72625, name: "Stavanger", firerisk: 5.123 },
      { lat: 58.1467, lng: 7.9956, name: "Kristiansand", firerisk: 4.923 },
      // { lat: 69.968086, lng: 23.271521, name: "Alta", firerisk: 10.212 },
    ];

    const initializeMap = () => {
      googleMap.current = new window.google.maps.Map(googleMapRef.current, {
        mapTypeId: window.google.maps.MapTypeId.HYBRID,
      });

      const bounds = new window.google.maps.LatLngBounds();

      // Create markers and InfoWindows
      markersData.forEach((markerData) => {
        const marker = new window.google.maps.Marker({
          position: { lat: markerData.lat, lng: markerData.lng },
          map: googleMap.current,
          icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        });

        // Create an InfoWindow
        const infoWindow = new window.google.maps.InfoWindow({
          content: `
          <div style="background-color: #1E1E1E; color: white; padding: 10px;">
            <h5 style="margin: 0; color: #F08726;">${markerData.name}</h5>
            <p style="margin: 0;"><strong>FireRisk:</strong> ${markerData.firerisk}</p>
            <p style="margin: 0;"><strong>Lat:</strong> ${markerData.lat}</p>
            <p style="margin: 0;"><strong>Lng:</strong> ${markerData.lng}</p>
          </div>
        `,
        });

        // Add a click event listener to the marker
        marker.addListener('click', () => {
          infoWindow.open(googleMap.current, marker);
        });

        // Extend the bounds to include the marker's position
        bounds.extend(marker.position);
      });

      // Fit the map to the bounds
      googleMap.current.fitBounds(bounds);
    };

    if (!window.google) {
      // Load Google Maps script
      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=${'AIzaSyCQI5iKUBZozRPj0TMYEPL6puVkTeqNgHA'}`;
      document.head.append(script);
      script.addEventListener('load', initializeMap);
      return () => script.removeEventListener('load', initializeMap);
    } else {
      initializeMap();
    }
  }, []);

  return <div id="google-map" ref={googleMapRef} />;
};

export default GoogleMaps;

// Possible implementation for an API-call method:
// import React, { useEffect, useRef, useState } from "react";
// import "./GoogleMaps.css";

// const GoogleMaps = () => {
//   const googleMapRef = useRef(null);
//   const googleMap = useRef(null);
//   const [markersData, setMarkersData] = useState([]);

//   useEffect(() => {
//     // Fetch data from API
//     fetch('http://your-api-url.com')
//       .then(response => response.json())
//       .then(data => setMarkersData(data))
//       .catch(error => console.error('Error:', error));
//   }, []);

//   useEffect(() => {
//     const initializeMap = () => {
//       googleMap.current = new window.google.maps.Map(googleMapRef.current, {
//         center: { lat: 59.772023, lng: 8.468946 },
//         zoom: 7,
//         mapId: process.env.REACT_APP_API_MAP_ID,
//       });

//       // Create markers and InfoWindows
//       markersData.forEach((markerData) => {
//         const marker = new window.google.maps.Marker({
//           position: { lat: markerData.lat, lng: markerData.lng },
//           map: googleMap.current,
//         });

//         const infoWindow = new window.google.maps.InfoWindow({
//           content: `${markerData.name}: ${markerData.firerisk}`,
//         });

//         marker.addListener("click", () => {
//           infoWindow.open(googleMap.current, marker);
//         });
//       });
//     };

//     if (!window.google) {
//       const script = document.createElement("script");
//       script.src = `https://maps.googleapis.com/maps/api/js?key=${process.env.REACT_APP_API_KEY_GOOGLE_MAPS}`;
//       script.async = true;
//       document.head.appendChild(script);
//       script.addEventListener("load", initializeMap);
//       return () => script.removeEventListener("load", initializeMap);
//     } else {
//       initializeMap();
//     }
//   }, [markersData]);

//   return <div id="google-map" ref={googleMapRef} />;
// };

// export default GoogleMaps;
