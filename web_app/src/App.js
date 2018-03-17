import React, { Component } from 'react';

import './App.css';


class App extends Component {

  myfunc(){
    console.log("got here");
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
