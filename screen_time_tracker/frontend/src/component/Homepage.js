import React, { Component } from "react";
import Hours from "./Hours";
import Navigation from "./Navigation";
import Category from "./Category";
import Settings from "./Settings";
import Usage from "./Usage";
import {
    BrowserRouter,
    Routes,
    Route,
    Redirect,
    Link
} from "react-router-dom";



export default class Homepage extends Component{
    constructor(props){
        super(props);
    }

    render(){
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigation />} />
                <Route path="/Hours" element={<Hours />}></Route>
                <Route path="/Category" element={<Category />}></Route>
                <Route path="/Usage" element={<Usage />}></Route>
                <Route path="/Settings" element={<Settings />}></Route>
            </Routes>
        </BrowserRouter>
    );
}
}