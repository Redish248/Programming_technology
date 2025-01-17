import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import { Router } from "react-router-dom"
import {createBrowserHistory} from 'history'
import * as serviceWorker from './serviceWorker';

const history = createBrowserHistory()

ReactDOM.render((
        <Router history={history}>
            <App/>
        </Router>
    ), document.getElementById('root')
);

serviceWorker.unregister();
