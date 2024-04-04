import "./Home.css";
import Logo from "../assets/FireGuard Logo.webp";

export default function Home() {
  return (
    <>
      <section id="homepage">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-6">
              <a id="logo"
                href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                target="_blank"
                rel="noopener noreferrer"
              >
                <img src={Logo} alt="FireGuard Logo" id="logo" />
              </a>
            </div>

            <div class="col-md-6">
              <h1 id="heading">FireGuard</h1>
              <h3 id="subheading">Dynamic Fire Risk Computational Model</h3>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
