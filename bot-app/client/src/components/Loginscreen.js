import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/Raisedbutton';

import Login from './Login';
import Register from '/Register';

class Loginscreen extends Component {
    constructor(props) {
        this.state={
            username:'',
            password:'',
            loginscreen:[],
            loginmessage:'',
            buttonLabel:'Register',
            isLogin:true
        }
    }
    componentWillMount(){
        var loginscreen=[];
        loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext}/>);
        var loginmessage = "Not registered yet, Register Now";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage
        })
    }
    render() {
        return (
            <div className="loginsceen">
                {this.state.loginscreen}
                <div>
                    {this.state.loginmessage}
                    <MuiThemeProvider>
                        <div>
                            <RaisedButton label={this.state.buttonLabel} primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                        </div>
                    </MuiThemeProvider>
                </div>
            </div>
        );
    }
}

const style = {
    margin: 15,
};

handleClick(event){
    // console.log("event",event);
    var loginmessage;
    if(this.state.isLogin){
        loginscreen.push(<Register parentContext={this} appContext={this.props.parentContext}/>);
        loginmessage = "Already registered.Go to Login";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage,
            buttonLabel:"Login",
            isLogin:false
        })
    }
    else{
        var loginscreen=[];
        loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext}/>);
        loginmessage = "Not Registered yet. Go to registration";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage,
            buttonLabel:"Register",
            isLogin:true
        })
    }
}