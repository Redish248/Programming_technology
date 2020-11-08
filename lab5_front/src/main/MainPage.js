import React, {Component} from "react";
import * as axios from "axios";
import {InputGroup} from "react-bootstrap";

class MainPage extends Component {

    constructor(props) {
        super(props);
        this.state = {
            level: 1,
        }
    }

    setUpLevel = (event) => {
        let that = this;
        event.preventDefault();
        let formData = new FormData();
        formData.set('level', this.state.level);
        axios({
            method: 'post',
            url: 'http://localhost:8080/game/send_level',
            data: formData,
            withCredentials: true
        }).catch(function (error) {
            console.log(error);
            if (error === undefined || error.response === undefined) {
                that.props.history.push('/ss');
            }
        });
    };

    render() {
        return (
            <div>
                <h2>Выберите уровень:</h2>
                <InputGroup className="mb-3">
                    <InputGroup>
                        <InputGroup.Prepend>
                            <InputGroup.Radio  />
                            1 - Лёгкий
                        </InputGroup.Prepend>
                        <InputGroup.Prepend>
                            <InputGroup.Radio />
                            2 - Средний
                        </InputGroup.Prepend>
                        <InputGroup.Prepend>
                            <InputGroup.Radio />
                            3 - Сложный
                        </InputGroup.Prepend>
                    </InputGroup>
                </InputGroup>
            </div>
        );
    }
}

export default MainPage;