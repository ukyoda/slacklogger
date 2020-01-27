import React from 'react'
// import { slackChannels } from '../store/store'

interface Props {
  wsid: String
}
interface States {}

export default class ChannelList extends React.Component<Props, States> {
  constructor(props: Props) {
    super(props)
  }

  render () {
    return <div>test</div>
  }

}
