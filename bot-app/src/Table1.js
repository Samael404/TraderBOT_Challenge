import React, { Component } from 'react';
import {BootstrapTable, 
       TableHeaderColumn} from 'react-bootstrap-table';
import "./components/Table1.css";
import '../../node_modules/react-bootstrap-table/css/react-bootstrap-table.css';

var data= [
  {User: 'Kevin', Date: 'xx/xx/xx', Version: '1.0', TimeRan: '3hrs', Transactions: '100', 
   OpenOrders: '1', StartValue: '$10000', EndValue: '$10100', Pecentofchange: "1%"}
];
 
 
class Table1 extends Component {
  render() {
    return (
      <div>
        <p className="Table-header">Trader_Bot_Results</p>
        <BootstrapTable data={data}>
          <TableHeaderColumn isKey 
                             dataField='User'
                             dataAlign= 'center'
                             headerAlign="left"
                             width="100">
                             
            User
          </TableHeaderColumn>
          <TableHeaderColumn dataField='Date'
                             dataAlign='center'
                             headerAlign='center'
                             width="200">
            Date
          </TableHeaderColumn>
          <TableHeaderColumn dataField='Version'
                             dataAlign='center'
                             headerAlign='center'
                             width="200">
            Version
          </TableHeaderColumn>
          <TableHeaderColumn dataField='TimeRan'
                             dataAlign='center'
                             headerAlign='center'
                             width="120">
          Time Ran  
          </TableHeaderColumn>
          <TableHeaderColumn dataField='Transactions'
                             dataAlign='center'
                             headerAlign='center'
                             width="250">
          Transactions
          </TableHeaderColumn>
          <TableHeaderColumn dataField='OpenOrders'
                             dataAlign='center'
                             headerAlign='center'
                             width="250">
          Open Orders                     
          </TableHeaderColumn>
          <TableHeaderColumn dataField='StartValue'
                             dataAlign='center'
                             headerAlign='center'
                             width="250">
          Start Value                   
          </TableHeaderColumn>
          <TableHeaderColumn dataField='EndValue'
                             dataAlign='center'
                             headerAlign='center'
                             width="250">
          End Value
          </TableHeaderColumn>
          <TableHeaderColumn dataField='Pecentofchange'
                             dataAlign='center'
                             headerAlign='center'
                             width="100">
          Percent of Change                                      
          </TableHeaderColumn>
        </BootstrapTable>
      </div>
    );
  }
}
 
export default Table1;