import React, {Component} from "react";
import * as axios from "axios";
import Image from 'react-bootstrap/Image'
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

class GamePage extends Component {

    constructor(props) {
        super(props);
        this.state = {
            level: 1,
            image: [],
            correct_name: 'a',
            varA: 'b',
            varB: 'c',
            selectedAnswer: '',
            result: ''
        }
    }

    componentDidMount() {
        let that = this;
        axios({
            method: 'get',
            url: 'http://localhost:8080/game/next_question',
            withCredentials: true
        }).then((res) => {
            console.log(res)
                this.setState({
                    image: res.data.image,
                    correct_name: res.data.correct_name,
                    varA: res.data.varA,
                    varB: res.data.varB,
                });
            }
        ).catch(function (error) {
            console.log(error);
            if (error === undefined || error.response === undefined) {
                that.props.history.push('/ss');
                window.location.reload()
            }
        });
    }

    onValueChange = (event) => {
        this.setState({
            selectedAnswer: event.target.value
        });
    }

    checkAnswer = () => {
        if (this.state.correct_name === this.state.selectedAnswer) {
            this.setState({
                result: 'Правильно!'
            });
        } else {
            this.setState({
                result: 'Неправильно!'
            });
        }

    }

    goNext = () => {
       // this.props.history.push('/game');
        window.location.reload()
    }

    render() {
        return (
            <div>
                <h3>Выберите ответ:</h3>
                <table >
                    <tr>
                        <td>
                            <Container>
                                <Row>
                                    <Col xs={300} md={200} >
                                        <Image className="marginAll" src={this.state.image} alt="Картинка не загрузилась" thumbnail />
                                    </Col>
                                </Row>
                            </Container>
                        </td>
                        <td>
                            <div>
                                <div className="radio">
                                    <label>
                                        <input
                                            type="radio"
                                            value={this.state.varA}
                                            checked={this.state.selectedAnswer === this.state.varA}
                                            onChange={this.onValueChange}
                                        />
                                        {this.state.varA}
                                    </label>
                                </div>
                                <div className="radio">
                                    <label>
                                        <input
                                            type="radio"
                                            value={this.state.varB}
                                            checked={this.state.selectedAnswer === this.state.varB}
                                            onChange={this.onValueChange}
                                        />
                                        {this.state.varB}
                                    </label>
                                </div>
                                <div className="radio">
                                    <label>
                                        <input
                                            type="radio"
                                            value={this.state.correct_name}
                                            checked={this.state.selectedAnswer === this.state.correct_name}
                                            onChange={this.onValueChange}
                                        />
                                        {this.state.correct_name}
                                    </label>
                                </div>
                                <Button className="marginAll" variant="secondary" size="lg" active onClick={this.checkAnswer} >
                                    Ответить
                                </Button>
                            </div>
                            <div className="marginAll" className="Error">{this.state.result}</div>
                            <div className="mb-2">
                                <Button className="marginAll" variant="secondary" size="lg" onClick={this.goNext}>
                                    Дальше
                                </Button>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        );
    }
}

export default GamePage;