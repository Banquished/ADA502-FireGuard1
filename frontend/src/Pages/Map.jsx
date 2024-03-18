import "./Map.css";
import GoogleMaps from "../Components/GoogleMaps.jsx";

export default function Map() {
  return (
    <>
      <section>
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-4">
              <div class="row default-styling">
                <h3>FireGuard Map Integration</h3>
                <p>FireGuard is a ...</p>
              </div>
              <div class="row default-styling">
                <h3>FireGuard Locations</h3>
                <p>Locations are Coming...</p>
              </div>
            </div>
            <div class="col-md-8">
              <GoogleMaps />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
