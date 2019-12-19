import React from 'react'
import "bootstrap/dist/css/bootstrap.min.css";

interface LayoutProp {
  children: any
}

const Layout = (props: LayoutProp) => {
  return ( <div> { props.children } </div> )
}

export default Layout
