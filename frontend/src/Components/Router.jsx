import { BrowserRouter, Routes, Route, Outlet } from "react-router-dom";
import Home from "../Pages/Home.jsx";
import Map from "../Pages/Map";
import About from "../Pages/About";
import Contact from "../Pages/Contact";

export default function Router() {
  const Layout = () => {
    return (
      <>
        <Outlet />
      </>
    );
  };

  const BrowserRoutes = () => {
    return (
      <>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />} />
              <Route index element={<Home />} />
              <Route path="map" element={<Map />} />
              <Route path="about" element={<About />} />
              <Route path="contact" element={<Contact />} />
          </Routes>
        </BrowserRouter>
      </>
    )
  }

  return (
    <>
      <BrowserRoutes />
    </>
  );
}
