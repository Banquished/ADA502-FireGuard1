import "./About.css";
import GitHubIcon from "@mui/icons-material/GitHub";
import Button from "@mui/material/Button";

export default function About() {
  return (
    <>
      <section>
        <div class="container">
          <div class="row text">
            <div>
              <h3>
                <b>FRCM-module credits</b>
              </h3>
              <p>
                The DYNAMIC Fire Risk Indicator Implementation repository
                contains the implementation of the dynamic risk indicator
                described in the submitted paper:
              </p>
              <p>
                R.D: Strand and L.M. Kristensen.&nbsp;
                <i>
                  "An implementation, evaluation and validation of a dynamic
                  fire and conflagration risk indicator for wooden homes."
                </i>{" "}
                <br />
                Submitted for review.
              </p>
              <p>
                FRCM uses forecast and weather data observation for computing
                fire risk indication in the form of time-to-flash-over (ttf) for
                wooden houses.
              </p>

              <a
                href="https://github.com/Banquished/dynamic-frcm"
                alt="Link to FRCM-module"
              >
                <Button
                  variant="contained"
                  color="warning"
                  startIcon={<GitHubIcon />}
                >
                  GitHub Repository
                </Button>
              </a>
            </div>
          </div>
          <div class="row text">
            <h3>
              <b>About the ADA502 Project</b>
            </h3>
            <p>
              The Course ADA502 has a project going the whole semester, where
              the goal is for students to further work on the FRCM-module and
              create a service that is ready to be deployed to the Cloud. This
              includes:
              <ul>
                <li>Setting up a frontend web-application</li>
                <li>Refactoring existing code to fit the course description</li>
                <li>Looking at CI/CD Pipelines</li>
                <li>Configuring a working API to connect to the frontend</li>
                <li>Storing data in databases</li>
              </ul>
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
