import React , { Component } from "react";
import { render } from "react-dom";
import Homepage from "./component/Homepage";
import Navigation from "./component/Navigation";
import About from "./component/About"

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div>
            <Homepage />
            <About />
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)