import React, { Component } from 'react';

import Table from "./components/Table1.js";

var data = [
    {id: 1, date: 'xx/xx/xx', value: '1'},
    {id: 1, date: 'xy/xy/xy', value: '2'},
    {id: 1, date: 'yy/yy/yy', value: '3'},    
];

class Results extends Component {
    render() {
        return (
            <div className="Results">
                <p className="Table-header">Results</p>
                <Table1 data={data}/>
            </div>
        );
    }
}

export default Results;