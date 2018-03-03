import React, { Component } from "react";
import { Route, Link, BrowserRouter } from 'react-router-dom';

class Header extends Component {
    render() {
        return(
            <div>
                <h1>TraderBot_Challange</h1>
                <ul className="header">
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/Page1">Page1</Link></li>
                    <li><Link to="/Page2">Page2</Link></li>
                    <li><Link to="/LeaderBoard">LeaderBoard</Link></li>
                </ul>
            </div>
        );
    }
}

export default Header;
