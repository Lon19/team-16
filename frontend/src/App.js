import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import ProgressBar from 'react-bootstrap/ProgressBar';

class App extends React.Component {
  render() {
    return (
      <div>
        <Container>
            <Header/>
            <HPBar/>
            <Money/>
            <StoryCard/>
            <BottomNavigation/>
        </Container>
      </div>
    );
  }
}

class Header extends React.Component {
  render() {
    return (
      <div>
        <h1>CLIC Sargent</h1>
      </div>
    );
  }
}

class HPBar extends React.Component {
  render() {
    return (
      <ProgressBar now={60} />
    );
  }
}

class Money extends React.Component {
  render() {
    return (
      <ion-icon name="cash"></ion-icon>
    );
  }
}

class StoryCard extends React.Component {
  render() {
    return (
      <Card style={{ width: '18rem' }}>
        <Card.Body>
          <Card.Title>Start your mission</Card.Title>
          <Card.Text>
            Which planet do you want to explore???
          </Card.Text>
          <Row>
            <Col><Button variant="primary">Venus</Button></Col>
            <Col><Button variant="primary">Mars</Button></Col>
          </Row>
        </Card.Body>
      </Card>
    );
  }
}

class BottomNavigation extends React.Component {
  render() {
    return (
      <Navbar fixed="bottom" >
        <Nav.Link href='#games'>Games</Nav.Link>
        <Nav.Link href='#home'>Home</Nav.Link>
        <Nav.Link href='#chat'>Chat</Nav.Link>
      </Navbar>
    );
  }
}

export default App;
