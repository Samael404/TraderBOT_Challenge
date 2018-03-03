import React, { Component } from "react";
import { render } from 'react-dom';
import { Route, Router, } from 'react-router-dom';
import About from "./About";
import Daily from "./Daily";
import History from "./History";

class Header extends Component {
    render() {
        return (
            <Router>
                <div>
                    <hl>Trader_Bot_Challange</hl>
                    <ul className="header">
                        <li><Route path="/About" component={About}/></li>
                        <li><Route path="/Daily" component={Daily}/></li>
                        <li><Route path="/History" component={History}/></li>
                    </ul>
                </div>
            </Router>
        );
    }

}

export default Header;