import React from "react";
import ReactDOM from "react-dom";

var element1 = React.createElement("h1",{id: "id_001", className: "main_title"}, "Hello world");
ReactDOM.render(element1, document.getElementById("container"));