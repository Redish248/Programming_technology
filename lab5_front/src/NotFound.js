
import React, { Component} from 'react';
import {Button} from "primereact/components/button/Button";

class NotFound extends Component{

    constructor(props) {
        super(props);
    }

    handlePrevPage = () => {
        this.props.history.push('/');
    };
    render() {
        return (
            <div className="NotFound">
                <h2>Такой страницы не существует</h2>
                <h2>Возможно, сервер не отвечает</h2>
                <iframe src="https://giphy.com/embed/XgDozI2ewprHO" width="300" height="300" frameBorder="1" className="giphy-embed" allowFullScreen/>
                <p>
                    <a href="https://giphy.com/gifs/pusheen-XgDozI2ewprHO"/>
                </p>
                <Button label="На главную" onClick={this.handlePrevPage}/>

            </div>
        );
    }
}

export default NotFound;