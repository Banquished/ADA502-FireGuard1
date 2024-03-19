"use client";
import "./GoogleMaps.css";
import { useState } from "react";
import {
  APIProvider,
  Map,
  AdvancedMarker,
  Pin,
  InfoWindow,
} from "@vis.gl/react-google-maps";

export default function GoogleMaps() {
  const position = { lat: 60.472023, lng: 8.468946 };
  const [open, setOpen] = useState(false);

  return (
    <APIProvider apiKey={process.env.REACT_APP_API_KEY_GOOGLE_MAPS}>
      <div style={{ height: "80vh" }}>
        <Map
          zoom={7}
          center={position}
          mapId={'65e630946553510a'}
        >
          <AdvancedMarker position={position} onClick={() => setOpen(true)}>
            <Pin background={"red"} borderColor={"black"} glyphColor={"orange"} />
          </AdvancedMarker>
          {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
              <p style={{color: "black"}}>FireRisk: 5.4123</p>
            </InfoWindow>
          )}

          <AdvancedMarker position={position} onClick={() => setOpen(true)}>
            <Pin background={"red"} borderColor={"black"} glyphColor={"orange"} />
          </AdvancedMarker>
          {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
              <p style={{color: "black"}}>FireRisk: 5.4123</p>
            </InfoWindow>
          )}
        </Map>
      </div>
    </APIProvider>
  );
}
