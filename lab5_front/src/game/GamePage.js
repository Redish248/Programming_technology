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
            correct_answer: 'a',
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
                    correct_answer: res.data.correct_answer,
                    varA: res.data.varA,
                    varB: res.data.varB,
                });
            }
        ).catch(function (error) {
            console.log(error);
            if (error === undefined || error.response === undefined) {
                that.props.history.push('/ss');
            }
        });
    }

    onValueChange = (event) => {
        this.setState({
            selectedAnswer: event.target.value
        });
    }

    checkAnswer = () => {
        if (this.state.correct_answer === this.state.selectedAnswer) {
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
        this.props.history.push('/game');
    }

    render() {
        return (
            <div>
                <h3>Выберите ответ:</h3>
                <table>
                    <tr>
                        <td>
                            <Container>
                                <Row>
                                    <Col xs={6} md={4}>
                                        <Image src={this.state.image} alt="Картинка не загрузилась" thumbnail />
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
                                            value={this.state.correct_answer}
                                            checked={this.state.selectedAnswer === this.state.correct_answer}
                                            onChange={this.onValueChange}
                                        />
                                        {this.state.correct_answer}
                                    </label>
                                </div>
                                <Button variant="secondary" size="lg" active onClick={this.checkAnswer} >
                                    Ответить
                                </Button>
                            </div>
                            <div className="Error">{this.state.result}</div>
                            <div className="mb-2">
                                <Button variant="secondary" size="lg" onClick={this.goNext}>
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