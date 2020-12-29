import React from "react";
import { Link } from "react-router-dom";
import Menu from "./Menu";

function Header() {
  return (
    <header className="fixed bg-white shadow-md top-0 w-full z-40">
        <Menu/>
        <div
          className="flex justify-center"
          >
          <Link to="/">
            Mock Fashion
          </Link>
        </div>
      <div className="flex justify-center">
        <Link to="/collection" className="mr-4 hover:text-gray-600">collection</Link>
        <Link to="/inspire" className="mr-4 hover:text-gray-600">community</Link>
      </div>
    </header>
  );
}

export default Header;