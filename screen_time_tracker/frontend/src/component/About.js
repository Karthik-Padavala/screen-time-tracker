import React, { Component } from "react";
import { FaHeart } from "react-icons/fa";

export default class About extends Component{
    constructor(props){
        super(props);
    }

    render(){
    return (
        <div class="about">
            <h3>Made with  <FaHeart /></h3>
        </div>
    );
}
}