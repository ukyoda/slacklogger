import {Navbar, Nav} from 'react-bootstrap'
import React from 'react'

interface Props {}
interface States {}

export default class SideMenu extends React.Component<Props, States> {
  constructor(props: Props) {
    super(props)
  }
  render () {
    return (
      <div className="bg-dark" style={{minWidth: '250px'}}>
        <Navbar bg="dark" expand="lg" variant="dark" >
          <Navbar.Brand>メニュー</Navbar.Brand>
        </Navbar>
        <Navbar bg="dark" expand="lg" variant="dark" >
          <Nav defaultActiveKey="/home" className="flex-column text-white navbar-dark">
            <Navbar.Text>Workspaces</Navbar.Text>
            <Nav.Link href="/home" className="text-white">
              Active
            </Nav.Link>
            <Nav.Link eventKey="link-1">Link</Nav.Link>
            <Nav.Link eventKey="link-2">Link</Nav.Link>
            <Nav.Link eventKey="disabled" disabled>
              Disabled
            </Nav.Link>
          </Nav>
        </Navbar>
      </div>
    );
  }
}
