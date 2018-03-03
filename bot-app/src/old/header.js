import React, { Component } from "react";
import { Route, Link, BrowserRouter } from 'react-router-dom';

class Header extends Component {
    render() {
        return(
            <HashRouter>
                <div>
                    <h1>TraderBot_Challange</h1>
                    <ul className="header">
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/About">About</Link></li>
                        <li><Link to="/History">History</Link></li>
                        <li><Link to="/Challange">Challange</Link></li>
                        <li><Link to="/Price">Price</Link></li>
                        <li><Link to="/LeaderBoard">Leaderboard</Link></li>
                    </ul>
                </div>
            </HashRouter>   
        );
    }
}

export default Header;
