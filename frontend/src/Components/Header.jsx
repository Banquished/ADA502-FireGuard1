import Button from "@mui/material/Button";
import "./Header.css";


export default function Header() {
  return (
    <nav id="header-background">
      <h1 id="heading-title">FireGuard</h1>
      <ul className="right">
        <Button variant="contained" color="warning" href="/">Home</Button>
        <Button variant="contained" color="warning" href="/map">Map</Button>
        <Button variant="contained" color="warning" href="/about">About</Button>
        <Button variant="contained" color="warning" href="/contact">Contact</Button>
      </ul>
    </nav>
  );
}
