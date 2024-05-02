import React, { useEffect, useRef } from "react";
import axios from 'axios';
import "./GoogleMaps.css";

const GoogleMaps = () => {
  const googleMapRef = useRef(null);
  const googleMap = useRef(null);

  useEffect(() => {
    const initializeMap = (markersData) => {
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
            <p style="margin: 0;"><strong>StationId:</strong> ${markerData.station_id}</p>
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
      script.async = true;
      script.src = `https://maps.googleapis.com/maps/api/js?key=${'AIzaSyCQI5iKUBZozRPj0TMYEPL6puVkTeqNgHA'}`;
      document.head.append(script);
      script.addEventListener('load', () => fetchMarkersData(initializeMap));
      return () => script.removeEventListener('load', () => fetchMarkersData(initializeMap));
    } else {
      fetchMarkersData(initializeMap);
    }
  }, []);

  const fetchMarkersData = (callback) => {
    axios.get('http://localhost:8000/apicall/weatherstations/')
      .then(response => {
        const markersData = response.data.map(item => ({
          lat: parseFloat(item.latitude),
          lng: parseFloat(item.longitude),
          name: item.city,
          firerisk: item.prediction,
          station_id: item.station_id
        }));
        callback(markersData);
      })
      .catch(error => console.error(error));
  };

  return <div id="google-map" ref={googleMapRef} />;
};

export default GoogleMaps;