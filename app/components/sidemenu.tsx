import {Navbar, Nav} from 'react-bootstrap'
import React from 'react'
import { observer } from 'mobx-react'
import { slackWorkspaces } from '../store/store'
import Link from 'next/link'

interface Props {}
interface States {}

@observer
export default class SideMenu extends React.Component<Props, States> {
  constructor(props: Props) {
    super(props)
  }

  componentDidMount () {
    if (slackWorkspaces.state !== 'done') {
      slackWorkspaces.fetch()
    }
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
            { (slackWorkspaces.state == 'done') && this.renderList() }
            <Nav.Link as="span">
              <i className="fa fa-plus-square"></i> Add Workspace
            </Nav.Link>
          </Nav>
        </Navbar>
      </div>
    );
  }

  renderList () {
    return slackWorkspaces.workspaces.map((value, index) => {
      const key = `item-${index}`
      const linkAs = `/ws/${value.id}`
      const link = '/ws/[wsid]'
      const name = value.name
      return (
        <Nav.Link as="span" key={key}>
          <Link href={link} as={linkAs}>
            <a className="text-light">{name}</a>
          </Link>
        </Nav.Link>
      );
    })
  }
}
