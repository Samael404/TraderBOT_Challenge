import React, { Component } from 'react';
import MuithemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';

class Login extends Component {
    constructor(props) {
        super(props);
        this.state={
            username:'',
            password:''
        }
    }
    render(){
        return (
            <div>
                <MuiThemeProvider>
                    <div>
                        <AppBar
                            title="Login"
                        />
                        <TextField
                            hintText="Enter your Username"
                            floatingLabelText="Username"
                            onChange = {(event,newValue) => this.setState({username:newValue})}
                        />
                        <br/>
                        <TextField
                            Type="password"
                            hintText="Enter your Password"
                            floatingLabeltext="Password"
                            onChange = {(event,newValue) => this.setState({password:newValue})}
                        />
                        <br/>
                        <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>            
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
    var apiBaseUrl = "http://localhost:5000/api/";
    var self = this;
    var payload={
    "username":this.state.username,
    "password":this.state.password
    }
    axios.post(apiBaseUrl+'login', payload)
    .then(function (response) {
        console.log(response);
        if(response.data.code == 200){
            console.log("Login successful");
        var uploadScreen=[];
        uploadScreen.push(<UploadScreen appContext={self.props.appContext}/>)
        self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})    
        }
        else if(response.data.code ==204){
            console.log("Username password do not match");
            alert("username password do not match")
        }
        else{
            console.log("Username does not exist");
            alert("username does not exist");
        }     
    })
    .catch(function (error){
        console.log(error);
    });
}

export default Login;