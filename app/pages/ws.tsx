import * as React from 'react'
import SlackAPI from '../libs/SlackAPI'
import * as SlackAPITypes from '../libs/types/slackAPI';

interface Props {}
interface State {
  api: SlackAPI
  workspaces : SlackAPITypes.SlackWorkspace[]
}

export default class Workspaces extends React.Component<Props, State> {
  public state: State = {
    api: new SlackAPI(),
    workspaces: []
  }

  public async componentDidMount () {
    const workspaces = await this.state.api.workspaces();
    this.setState({ workspaces })
  }

  render () {
    return (
      <div>
        <ul>
          { 
            this.state.workspaces.map((ws: SlackAPITypes.SlackWorkspace, idx: number) => {
              return (
                <li key={idx}>
                  <pre>{ JSON.stringify(ws, null, '  ') }</pre>
                </li>
              )
            }) 
          }
        </ul>
      </div>
    )
  }
}
