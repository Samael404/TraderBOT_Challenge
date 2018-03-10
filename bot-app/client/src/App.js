import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import About from "./components/About";
import Price from "./components/Price";
import LeaderBoard from './components/LeaderBoard';
import Challange from "./components/Challange";
import Header from './components/header';

import './App.css';


const Home = () => <h1>Home</h1>;




class App extends Component {
  render() {
    return ( 
        <BrowserRouter>
            <div>
        
                <div className="Navbar">
                    <Header/>
                </div>
                
            <Route path='/' exact component={Home}/>
            <Route path='/About' component={About}/>
            <Route path='/Price' component={Price}/>
            <Route path='/LeaderBoard' component={LeaderBoard}/>
            <Route path='/Challange' component={Challange}/>
            </div>
        </BrowserRouter>
    );
  }
}



export default App;
