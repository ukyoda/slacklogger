import React from 'react'
import "@trendmicro/react-sidenav/dist/react-sidenav.css";

type LayoutProp = {
  children: any
}

const Layout = (props: LayoutProp) => {
  return ( 
    <div> { props.children } </div> 
  )
}

export default Layout
