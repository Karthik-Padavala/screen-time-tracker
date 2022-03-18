import React, { Component } from "react";
import Navigation from "./Navigation";

export default class Settings extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div>
                <Navigation />,
                <h1 class="heading">Adjust the Settings</h1>
            </div>
        );
    }
}