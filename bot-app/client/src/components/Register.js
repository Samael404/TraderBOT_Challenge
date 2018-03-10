import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/style/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from "/Login";

class Register extends Component {
    constructor(props){
        super(props);
        this.state={
            username:'',
            password:''
        }
    }

    render() {
        return (
            <div>
                <MuiThemeProvider>
                    <div>
                        <AppBar
                            title="Register"
                        />
                        <TextField
                            hintText="Enter your Username"
                            floatingLabelText="Username"
                            onChange = {(event,newValue) => this.setState({username:newValue})}
                        /> 
                        <br/>
                        <TextField
                            type = "password"
                            hintText="Enter your Password"
                            floatingLabelText="Password"
                            onChange = {(event,newValue) => this.setState({password:newValue})}
                        />
                        <br/>
                        <RaisedButton label="Subimit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>       
                    </div>
                </MuiThemeProvider>
            </div>
        );
    }
}

const style = {
    margin: 15,
};

handleClick(event) {
    var apiBaseUrl = "http://localhost:400/api/";
    console.log('values',this.state.username,this.state.password);
    var self = this;
    var payload={
        "username": this.state.username,
        "password": this.state.password
    }
    axios.post(apiBaseUrl+'/register',payload)
    .then(function (response);
    if(response.data.code == 200){
        //console.log("registration successful");
        var loginscreen=[];
        loginscreen.push(<Login parentContext={this} appContext={self.props.appContext}/>);
        var loginmessage = "Not Registered yet. Go to registration";
        self.props.parentContext.setState({loginscreen:loginscreen,loginmessage:loginmessage,
        buttonLabel:"Register",
        isLogin:true
        });
    }
.catch(function (error){
    console.log(error);
});
}

export default Register;