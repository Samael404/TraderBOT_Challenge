import React, { Component } from 'react';

import './App.css';


class App extends Component {

  myfunc(){
    console.log("got here");
    fetch('http://localhost:5000/login/josh', {
      mode: "no-cors",
      method: "GET",
      headers: {
        "Accept": "application/json"
      }
    })
    .then(results => {
      console.log(results);
      return results.json();
    })
    .then(results => {
      console.log(results);
    });
  };

  

  render() {
    return (
      <div>
        <div className="Button">Button
          <button onClick={this.myfunc}/>
        </div>
        <div>

        </div>
      </div>

    );
  }
}

export default App;
