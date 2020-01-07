import React from 'react'
// import { Container } from 'react-bootstrap'
import Sidebar from "react-sidebar";
import SideMenu from '../components/sidemenu';
import { Navbar } from 'react-bootstrap';
import Link from "next/link";
import getMQL from '../libs/utils/mediaquery';
interface State {
  sidebarOpen: boolean,
  sidebarDocked: boolean
}

export default class PageB extends React.Component<any, State> {
  public state:State = {
    sidebarOpen: true,
    sidebarDocked: true
  }

  get mql():MediaQueryList {
    return getMQL()
  }

  constructor (props: any) {
    super(props)
    this.onSetSidebarOpen = this.onSetSidebarOpen.bind(this)
    this.mediaQueryChanged = this.mediaQueryChanged.bind(this)
    this.onClickMenuIcon = this.onClickMenuIcon.bind(this)
  }

  onSetSidebarOpen(open: boolean) {
    this.setState({ sidebarOpen: open });
  }

  mediaQueryChanged () {
    if (this.mql !== null) {
      this.setState({ sidebarDocked: this.mql.matches, sidebarOpen: this.mql.matches });
    }
  }

  onClickMenuIcon (e: React.MouseEvent) {
    e.preventDefault()
    const currentState = this.state.sidebarOpen
    this.onSetSidebarOpen(!currentState)
  }

  componentDidMount() {
    this.setState({sidebarDocked: this.mql.matches})
    this.mql.addListener(this.mediaQueryChanged)
  }

  componentWillUnmount() {
    this.mql.removeListener(this.mediaQueryChanged);
  }

  render () {
    return (
      <Sidebar
        sidebar={<SideMenu />} // サイドバーのビュー
        sidebarClassName="bg-dark"
        docked={this.state.sidebarOpen}
        onSetOpen={this.onSetSidebarOpen}
        styles={{ sidebar: { background: "white" } }}
      >
        <div>
          <Navbar bg="dark" expand="lg" variant="dark" className="text-white">
            <Navbar.Brand>
              <span
                className="fas fa-bars"
                onClick={this.onClickMenuIcon}
                style={{ padding: "0 10px", cursor: "pointer" }}
              />
              <Link href="/">
                <a className="navbar-brand">Slackびゅ〜あ</a>
              </Link>
            </Navbar.Brand>
          </Navbar>
          <button
            onClick={() => this.onSetSidebarOpen(!this.state.sidebarOpen)}
          >
            Open sidebar
          </button>
        </div>
      </Sidebar>
    );
  }

}
