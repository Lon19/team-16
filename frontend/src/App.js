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
          <Row>
            <Container>
              <StoryCard game_id='{Math.floor((Math.random() * 1000) + 1)}' user_id='89'/>
            </Container>
          </Row>
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
        <h1 class="text-center">Space Mission!</h1>
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

class StoryCard extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.fetchOnClickLeft = this.fetchOnClickLeft.bind(this);
    this.fetchOnClickRight = this.fetchOnClickRight.bind(this);
  }
  componentDidMount() {
    fetch(`/${this.props.game_id}/${this.props.user_id}`)
    .then(data => data.json())
    .then((data) => {
      console.log(data)
      this.setState({title: data.name,
                     description: data.desc})
    }).catch(console.log)
  }

  state = {
    title: "Start Your Mission!!!!!!!!!",
    description: "mission commencing in ....."
  }

  fetchOnClickLeft = () => {
    fetch(`/${this.props.game_id}/left`)
    .then(data => data.json())
    .then((data) => {
      console.log(data)
      this.setState({title: data.name,
                     description: data.desc})
    }).catch(console.log)
  }

  fetchOnClickRight = () => {
    fetch(`/${this.props.game_id}/right`)
    .then(data => data.json())
    .then((data) => {
      console.log(data)
      this.setState({title: data.name,
                     description: data.desc})
    }).catch(console.log)
  }

  render() {
    return (
      <Card >
        <Card.Body>
          <Card.Title>{this.state.title}</Card.Title>
          <Card.Text>
            {this.state.description}
          </Card.Text>
          <Card.Img src="./image/4.jpg" />
          <Row>
            <Col><Button variant="primary" onClick={this.fetchOnClickLeft}>Venus</Button></Col>
            <Col><Button variant="primary" onClick={this.fetchOnClickRight}>Mars</Button></Col>
          </Row>
        </Card.Body>
      </Card>
    );
  }
}

class BottomNavigation extends React.Component {
  render() {
    return (
      <Container>
      <Navbar expand="lg" fixed="bottom" >
        <Nav.Link href='#games'>Games</Nav.Link>
        <Nav.Link href='#home'>Home</Nav.Link>
        <Nav.Link href='#chat'>Chat</Nav.Link>
      </Navbar>
      </Container>
    );
  }
}

export default App;
