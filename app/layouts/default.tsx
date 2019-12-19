import 'typeface-roboto';
import { AccessAlarm, ThreeDRotation } from '@material-ui/icons';
import React from 'react'

interface LayoutProp {
  children: any
}

const Layout = (props: LayoutProp) => {
  return ( <div> { props.children } </div> )
}

export default Layout