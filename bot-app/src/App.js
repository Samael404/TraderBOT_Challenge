import React, { Component } from 'react';
import './App.css';
import Header from "./components/header.js";
import StartButton from "./StartButton.js";
import Table1 from './Table1';



class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <StartButton />
        <br></br>
        <Table1 />
      </div>
    );
  }
}

export default App;