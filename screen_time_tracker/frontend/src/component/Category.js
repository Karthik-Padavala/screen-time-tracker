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

export default class Category extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div>
                <Navigation />,
                <h1 class="heading">Get your data for each category</h1>
            </div>
        );
    }
}