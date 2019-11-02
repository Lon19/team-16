import React, { Component } from "react";
import { MDBIcon } from "mdbreact";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Game from "./Game";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Chat from "./Chat";

function App() {
  return (
    <div>
      <Router>
        <div>
          <Route path='/' exact component={Home} />
          <Route path='/singleGame' component={GameDifficulty} />
          <Route path='/createMultiGame' component={MultiGame} />
          <Route path='/joinGame' component={JoinMultiGame} />
          <Route path='/chat' component={Chat} />
        </div>
      </Router>
    </div>
  );
}

function Home() {
  return <Navigations />;
}

function Navigations() {
  return (
    <div>
      <Container>
        <Row>
          <Col>
            <Link to='/singleGame'>Single Player</Link>
          </Col>
          <Col>
            <Link to='/chat'>
              <ion-icon name='chatboxes'></ion-icon>
            </Link>
          </Col>
        </Row>
        <br />
        <Row>
          <Col>
            <Link to='/singleGame'>Create Game</Link>
          </Col>
        </Row>
        <br />
        <Row>
          <Col>
            <Link to='/joinGame'>Join Game</Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

function JoinMultiGame() {
  return (
    <div>
      <Container>
        <Row>
          <Button variant='light'>
            <Link to='/createMultiGame'>Game ID: 91</Link>
          </Button>
        </Row>
      </Container>
    </div>
  );
}
function MultiGame() {
  return (
    <div>
      <Game />
    </div>
  );
}

function GameDifficulty() {
  return (
    <div>
      <Container>
        <Row>
          <Button variant='primary'>
            <Link to='/createMultiGame' style={{ color: "white" }}>
              Space Odyssey (Easy)
            </Link>
          </Button>
        </Row>
        <br />
        <Row>
          <Button variant='primary'>Monsters Inc (Medium)</Button>
        </Row>
        <br />
        <Row>
          <Button variant='primary'>Game of Thrones (Hard)</Button>
        </Row>
        <br />
      </Container>
    </div>
  );
}

export default App;
