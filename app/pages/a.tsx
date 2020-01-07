import React from 'react'
const SideNav = require('@trendmicro/react-sidenav')
const { NavItem, NavIcon, NavText } = SideNav
// import SideNav, { NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
// Be sure to include styles at some point, probably during your bootstraping

export default () => {
  return (
    <div>
      <SideNav onSelect={ (selected:any) => console.log(selected) } >
        <SideNav.Toggle />
        <SideNav.Nav defaultSelected="home">
          <NavItem eventKey="home">
            <NavIcon>
              <i className="fa fa-fw fa-home" style={{ fontSize: "1.75em" }} />
            </NavIcon>
            <NavText>Home</NavText>
          </NavItem>
          <NavItem eventKey="charts">
            <NavIcon>
              <i
                className="fa fa-fw fa-line-chart"
                style={{ fontSize: "1.75em" }}
              />
            </NavIcon>
            <NavText>Charts</NavText>
            <NavItem eventKey="charts/linechart">
              <NavText>Line Chart</NavText>
            </NavItem>
            <NavItem eventKey="charts/barchart">
              <NavText>Bar Chart</NavText>
            </NavItem>
          </NavItem>
        </SideNav.Nav>
      </SideNav>
      <div>
        abc
      </div>
    </div>
  );
}
