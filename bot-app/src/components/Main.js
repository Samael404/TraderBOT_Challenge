import React, { Component } from 'react';

class Main extends Component {
    render() {
        return(
            <div>
                <nav className="navbar navbar-default">
                    <div className="container-fluid">
                        <div className="navbar-header">
                            <a className="navbar-brand" href="App">Trader_Bot</a>
                        </div>
                        <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul className="nav navbar-nav">
                                <li className="active"><a href="Home">Link <span className="sr-only">(current)</span></a></li>
                                <li><a href="About">About</a></li>
                            </ul>
                        </div>
                    </div>            
                </nav>
            <div className="container">
                {this.props.children}
            </div>
        </div>        
        );
    }
}

export default Main