import React from 'react'

type LayoutProp = {
  children: any
}

const Layout = (props: LayoutProp) => {
  return ( 
    <div> { props.children } </div> 
  )
}

export default Layout
