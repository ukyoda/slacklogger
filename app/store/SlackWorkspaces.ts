import { observable, action, runInAction } from "mobx";
import axios from 'axios'

export type SlackWorkspace = {
  id: string
  name: string
  domain: string
  email_domain: string | null
  image_34: string
  image_44: string
  image_68: string
  image_88: string
  image_102: string
  image_132: string
  api_token: string
  active_flag: string
  delete_flag: boolean
  created_at: Date
  updated_at: Date
}

export class SlackWorkspaceList {
  private url = '/api/v1/slack/ws'
  @observable workspaces: SlackWorkspace[] = []
  @observable state:string = 'pending' // "pending" / "done" / "error"

  constructor() {
    this.find = this.find.bind(this)
  }

  @action.bound
  add(workspace: SlackWorkspace) {
    this.workspaces = [...this.workspaces, workspace]
  }

  @action.bound
  set(workspaces: SlackWorkspace[], append=false) {
    if (append) {
      this.workspaces = [...this.workspaces, ...workspaces]
    } else {
      this.workspaces = workspaces
    }
  }

  @action.bound
  async fetch() {
    this.state = 'pending'
    console.log(this.state);
    try {
      const res = await axios.get(this.url)
      runInAction(() => {
        this.state = 'done'
        this.set(res.data)
      })
    } catch (e) {
      runInAction(() => {
        this.state = "error";
        this.workspaces = []
      })
    }
  }

  find(id: string) {
    return this.workspaces.find((value) => value.id === id)
  }

}
