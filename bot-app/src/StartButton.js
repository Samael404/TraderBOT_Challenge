import React from 'react';

export default class StartButton extends React.Component {

    render(){
        return (
            <button onClick={this.props.start}>Start</button>
        )
    }
}