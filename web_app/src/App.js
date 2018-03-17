import React, { Component } from 'react';

import './App.css';


class App extends Component {
  constructor() {
    super();
    this.state = {
      'key': '',

    }
  }
  myfunc(){
    console.log("got here");
    fetch('http://localhost:5000/login/josh', {
      mode: "no-cors",
      method: "GET",
      headers: {
       "Content-type": "application/json"
      }
    })
    //.then(function(res){console.log(res.json())})
    .then((response) => response.json())
    .then((responseJSON) => {
      console.log(responseJSON);
    });
    
    /*
    .then(results => {
      console.log(results);
      return results.json();
    })
    .then(results => {
      console.log(results);
    })
    .catch(function(error){
      console.log(error);
    });
    this.setState({
      'key': 'testing123'
    }) */

  };

  

  render() {
    return (
      <div>
        <div className="Button">Button
          <button onClick={() => this.myfunc()}/>
        </div>
        <div>
          {this.state.key}
        </div>
      </div>

    );
  }
}

export default App;
