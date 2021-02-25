import React from 'react'
import { slackChannels } from '../store/store'
import { ListGroup } from 'react-bootstrap'
import Link from 'next/link'

interface Props {
  wsid: string
}
interface States {}

export default class ChannelList extends React.Component<Props, States> {
  constructor(props: Props) {
    super(props)
  }

  componentDidMount () {
    const wsid = this.props.wsid
    const state = slackChannels.state
    const isfetched = slackChannels.wsid === wsid 
    if (state !== 'done' || !isfetched) {
      slackChannels.fetch(wsid)
    }
  }

  render () {
    console.log(slackChannels.channels)
    return (<div>
      <h1>チャンネル一覧</h1>
      { (slackChannels.state == 'done') && this._renderList() }
    </div>)
  }

  _renderList () {
    return (<ListGroup>
      { slackChannels.channels.map((item, idx) => {
        const key = `channel-item-${idx}`
        const linkAs = `/ws/${item.id}`
        const link = '/ws/[wsid]/[chid]'
        const name = item.name
        return (
          <ListGroup.Item action key={key}>
            <Link href={link} as={linkAs}>
              <a className="text-dark">{name}</a>
            </Link>
          </ListGroup.Item>
        )
      }) }
    </ListGroup>)
  }

}
