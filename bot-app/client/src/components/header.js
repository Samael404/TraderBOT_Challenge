import React, { Component } from "react";
import { Link } from 'react-router-dom';

class Header extends Component {
    render() {
        return(
            <div>
                <br></br>
                <br></br>
                <h1>TraderBot_Challange</h1>
                <ul className="header">
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/About">About</Link></li>
                    <li><Link to="/Price">Current Price</Link></li>
                    <li><Link to="/LeaderBoard">LeaderBoard</Link></li>
                    <li><Link to="/Challange">Challange</Link></li>
                </ul>
            </div>
        );
    }
}

export default Header;
