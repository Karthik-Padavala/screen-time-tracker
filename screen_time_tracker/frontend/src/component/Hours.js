import React, { Component, useState } from "react";
import Navigation from "./Navigation";

import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from "@mui/material/Button";
import { keys } from "@mui/system";
import Category from "./Category";



class Hours extends Component{
    constructor(props){
        super(props);
        this.state = {
            value : 0,
            dat : {}
        };
        this.handleChange = this.handleChange.bind(this);
    };
    
    handleChange(e){
        this.setState({value : e.target.value});
        const hoursRequest = {
            method : "POST",
            headers:{"Content-Type" : "application/json"},
            body:JSON.stringify({"hours" : e.target.value}),
            };
        fetch('/tracker/hours', hoursRequest)
            .then((response) => response.json())
            .then((data) => this.setState({dat : data}));
    }
    
    createCategory(){
        let ass = Object.keys(this.state.dat)
        return ass.map((key, index) => {
            return <tr key={index}>{key}</tr>
        })
    }
    createTime(){
        let ass = Object.keys(this.state.dat)
        return ass.map((key, index) => {
            return <tr key={index}>{this.state.dat[key]}</tr>
        })

    }
    render(){
        const data = this.data
        return(
            <div>
                <Navigation />
                <div>
                    <h1 class="heading">Get your data for each hour </h1>
                </div>
                <Box class="heading">
                    <FormControl sx={{minWidth : 120}}>
                        <InputLabel>Hours</InputLabel>
                            <Select label="Hour" onChange={this.handleChange}>
                                <MenuItem value={1} sx={{color : "white"}}>1</MenuItem>
                                <MenuItem value={2} sx={{color : "white"}}>2</MenuItem>
                                <MenuItem value={3} sx={{color : "white"}}>3</MenuItem>
                                <MenuItem value={6} sx={{color : "white"}}>6</MenuItem>
                                <MenuItem value={12} sx={{color : "white"}}>12</MenuItem>
                                <MenuItem value={24} sx={{color : "white"}}>24</MenuItem>
                            </Select>
                    </FormControl>
                </Box>
                <h2 class="heading">Hours selected {this.state.value}</h2>
                <h3 class="heading">Brave : {this.state.dat["Brave"]}</h3>
                <table>
                    <tbody>
                        <tr>
                        <td>{this.createCategory()}</td>   
                        <td>{this.createTime()}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
                
        );
    }
}

export default Hours
