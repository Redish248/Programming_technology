import React, {Component} from "react";
import * as axios from "axios";
import Image from 'react-bootstrap/Image'
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import '../App.css';

class GamePage extends Component {

    constructor(props) {
        super(props);
        this.state = {
            level: 1,
            image: [],
            correct_name: 'a',
            varA: 'b',
            varB: 'c',
            varC: 'd',
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
            let answers = [res.data.varA, res.data.varB, res.data.correct_name]
            answers.sort();
            this.setState({
                image: res.data.image,
                correct_name: res.data.correct_name,
                varA: answers[0],
                varB: answers[1],
                varC: answers[2]
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
                result: 'Correct!'
            });
        } else {
            this.setState({
                result: 'Incorrect!'
            });
        }

    }

    goNext = () => {
        setTimeout(window.location.reload(), 1000)
    }

    render() {
        return (
            <div className="marginTop80">
                <h2>Choose an answer:</h2>
                <table >
                    <tr>
                        <td>
                            <Container>
                                <Row>
                                    <Col >
                                        <Image height={200} width={300} className="marginAll" src={this.state.image} alt="Картинка не загрузилась" thumbnail />
                                    </Col>
                                </Row>
                            </Container>
                        </td>
                        <td className="paddingLeft70">
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
                                            value={this.state.varC}
                                            checked={this.state.selectedAnswer === this.state.varC}
                                            onChange={this.onValueChange}
                                        />
                                        {this.state.varC}
                                    </label>
                                </div>
                                <Button className="marginAll" variant="secondary" size="lg" active onClick={this.checkAnswer} >
                                    Answer
                                </Button>
                            </div>
                            <div className="marginAll" className="Error">{this.state.result}</div>
                            <div className="mb-2">
                                <Button className="marginAll" variant="secondary" size="lg" onClick={this.goNext}>
                                    Next
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