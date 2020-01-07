
import { SlackWorkspace } from './types/slackAPI'
import axios from 'axios'

export default class SlackAPI {
  private baseURL: string;

  constructor () {
    if (this.isServerSide) {
      this.baseURL = 'http://localhost:3000/api/v1/slack'
    } else {
      this.baseURL = '/api/v1/slack';
    }
  }

  public async workspaces (): Promise<SlackWorkspace[]> {
    const url = `${this.baseURL}/ws`
    const res = await axios.get<SlackWorkspace[]> (url)
    return res.data;
  }

  private get isServerSide (): boolean {
    return typeof window === 'undefined'
  }
}
