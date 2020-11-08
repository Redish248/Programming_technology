import React from "react";
import { Route, Switch } from "react-router-dom";
import MainPage from "./main/MainPage";
import GamePage from "./game/GamePage";
import NotFound from "./NotFound";

export default () =>
    <Switch>
        <Route path="/game" exact component={GamePage} />
        <Route path="/" exact component={MainPage} />
        <Route component={NotFound} />
    </Switch>;