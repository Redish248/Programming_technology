import React, {Component} from "react";
import * as axios from "axios";
import Button from 'react-bootstrap/Button'
import '../App.css';

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
        }).then((res) => {
            window.location.replace('/game')
        }).catch(function (error) {
            console.log(error);
            if (error === undefined || error.response === undefined) {
                that.props.history.push('/ss');
                window.location.reload()
            }
        });
    };

    onValueChange = (event) => {
        this.setState({
            level: event.target.value
        });
    }

    render() {
        return (
            <div className="marginTop80">
                <h1>Game "Guess by the photo!"</h1>
                <form onSubmit={this.setUpLevel}>
                    <div className="radio">
                        <label>
                            <input
                                type="radio"
                                value="1"
                                checked={this.state.level === "1"}
                                onChange={this.onValueChange}
                            />
                            Level 1 - Light
                        </label>
                    </div>
                    <div className="radio">
                        <label>
                            <input
                                type="radio"
                                value="2"
                                checked={this.state.level === "2"}
                                onChange={this.onValueChange}
                            />
                            Level 2 - Medium
                        </label>
                    </div>
                    <div className="radio">
                        <label>
                            <input
                                type="radio"
                                value="3"
                                checked={this.state.level === "3"}
                                onChange={this.onValueChange}
                            />
                            Level 3 - Hard
                        </label>
                    </div>
                    <Button variant="secondary" size="lg" active type="submit">
                        Choose
                    </Button>
                </form>
            </div>
        );
    }
}

export default MainPage;