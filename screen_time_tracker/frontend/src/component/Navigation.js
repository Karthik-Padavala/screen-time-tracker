import React, { Component } from "react";
import Hours from "./Hours";
import Homepage from "./Homepage";
import Category  from "./Category";
import Settings from "./Settings";
import Usage from "./Usage";

export default class Hour extends Component{
    constructor(props){
        super(props);
    }

    render(){
    return (
        <div>
            <ul>
                <li class="left_align"><a href="">Home</a></li>
                <li class="left_align"><a href="Category">Category</a></li>
                <li class="left_align"><a href="Hours">Hour</a></li>
                <li class="left_align"><a href="Usage">Usage</a></li>
                <li class="right_align"><a href="Settings">Settings</a></li>
            </ul>
        </div>
    );
}
}