import React, { Component } from "react";

class History extends Component {
    render () {
        return (
            <div>
                <p>when using this page you can see the history of runs that have been done</p>
                {/* ToDo create a link to database to retrive the last time ran and version */}
            </div>
        );
    }
}

export default History;