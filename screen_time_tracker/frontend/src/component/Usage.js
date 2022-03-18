import React, { Component } from "react";
import Navigation from "./Navigation";

import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from "@mui/material/Button";
import { keys } from "@mui/system";
import Category from "./Category";

export default class Usage extends Component{
    constructor(props){
        super(props);
        this.state = {
            value : "",
            dat : {}
        };
        this.handleChange = this.handleChange.bind(this);
    };

    handleChange(e){
        this.setState({value : e.target.value});
        const usageRequest = {
            method : "POST",
            headers : {"Content-Type" : "application/json"},
            body : JSON.stringify({"usage" : e.target.value}),
        };
        fetch('/tracker/usage', usageRequest)
        .then((response) => response.json())
        .then((data) => this.setState({dat : data}));
        console.log(this.state.dat)
    }

    render(){
        return(
            <div>
                <Navigation />
                <h1 class="heading">Daily Usage </h1>
                <Box class="heading">
                    <FormControl sx={{minWidth : 120}}>
                        <InputLabel>Usage</InputLabel>
                            <Select label="Hour" onChange={this.handleChange}>
                                <MenuItem value={"today"} sx={{color : "white"}}>Today</MenuItem>
                                <MenuItem value={"this week"} sx={{color : "white"}}>This week</MenuItem>
                                <MenuItem value={"last two weeks"} sx={{color : "white"}}>2 weeks</MenuItem>
                                <MenuItem value={"this month"} sx={{color : "white"}}>This month</MenuItem>
                                <MenuItem value={"last three months"} sx={{color : "white"}}>3 months</MenuItem>
                                <MenuItem value={"from start"} sx={{color : "white"}}>From the begining</MenuItem>
                            </Select>
                    </FormControl>
                </Box>
            </div>
        );
    }
}