import "./Map.css";
import GoogleMaps from "../Components/GoogleMaps.jsx";
import List from '@mui/material/List';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';

export default function Map() {

  return (
    <>
      <section>
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-4">
              <div class="row default-styling">
                <h3>Maps Integration</h3>
                <p>
                  FireGuard is a web application that allows users to track and
                  monitor the fire risk for their homes. Users can view the
                  location of their homes on a map and receive notifications
                  when time to flashover is below a certain threshold near the
                  specified location. With FireGuard, users can stay informed
                  and take action to protect themselves from the threat of
                  fires.
                </p>
              </div>
              <div class="row default-styling">
                <h3>FireGuard Locations</h3>
                <p>
                  The FireGuard Project is still in beta. For you as an end-user
                  that means we're only providing risk calculations for the
                  following locations:
                </p>
                <List
                sx={{ width: '100%', maxWidth: 360 }}>
                  <ListItemText>Oslo</ListItemText>
                  <Divider/>
                  <ListItemText>Bergen</ListItemText>
                  <Divider/>
                  <ListItemText>Stavanger</ListItemText>
                  <Divider/>
                  <ListItemText>Kristiansand</ListItemText>
                  <Divider/>
                </List>
                <p>
                  <br />
                  We're working hard to expand our coverage to more locations.
                  If you have suggestions for our next expansion, please contact
                  us.
                </p>
              </div>
            </div>
            <div class="col-md-8 map">
              <GoogleMaps />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
