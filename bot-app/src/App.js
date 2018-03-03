import React, { Component } from 'react';
import { BrowserRouter, Route, Link} from 'react-router-dom';

import Header from './components/header'
import './App.css';

const Home = () => <h1>Home</h1>;
const Page1 = () => <h1>Page1</h1>;
const Page2 = () => <h1>Page2</h1>;

class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div>
                <div className="Navbar">
                    <Header/>
                </div>
            <Route path='/' component={Home}/>
            <Route path='/page1' component={Page1}/>
            <Route path='/page2' component={Page2}/>
            </div>
        </BrowserRouter>
    );
  }
}

export default App;
