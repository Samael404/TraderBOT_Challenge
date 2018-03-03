import React, { Component } from "react";
import {
    Route,
    Link,
    HashRouter,
} from 'react-router-dom';
import About from "./About";
import History from "./History";
import Challange from "./Challange";
import Price from "./Price";
import LeaderBoard from "./LeaderBoard";




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
                    <div className="content">
                        <Route path="/About" component={About}/>
                        <Route path="/History" component={History}/>
                        <Route path="/Challange" component={Challange}/>
                        <Route path="/Price" component={Price}/>
                        <Route path="/LeaderBoard" component={LeaderBoard}/> 
                    </div>           
                </div>
            </HashRouter>   
        );
    }
}

export default Header;