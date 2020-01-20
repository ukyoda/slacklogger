import { observable, action, runInAction } from 'mobx'
import axios from 'axios'
import { SlackWorkspace } from './SlackWorkspaces'

export type SlackChannel = {
  id: string
  local_id: string
  team_id: string
  name: string
  created: Date
  topic: string | null
  purpose: string | null
  delete_flg: boolean
  created_at: Date
  updated_at: Date
  workspace: SlackWorkspace
}

export class SlackChannelList {
  private url = '/api/v1/slack/ch'
  @observable channels: SlackChannel[] = []
  @observable state:string = 'pending'
  constructor() {
    this.find = this.find.bind(this)
  }

  @action.bound
  add(channel: SlackChannel) {
    this.channels = [...this.channels, channel]
  }

  @action.bound
  set(channels: SlackChannel[], append=false) {
    if (append) {
      this.channels = [...this.channels, ...channels]
    } else {
      this.channels = channels
    }
  }

  @action.bound
  async fetch(workspaceId: string) {
    const url = `${this.url}/${workspaceId}`
    this.state = 'pending'
    try {
      const res = await axios.get(url)
      runInAction(() => {
        this.state = 'done'
        this.set(res.data)
      })
    } catch (e) {
      runInAction(() => {
        this.state = 'error'
        this.channels = []
      })
    }
  }

  find (id: string) {
    return this.channels.find((value) => value.id === id)
  }

}
