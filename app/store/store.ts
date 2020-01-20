import { SlackWorkspaceList } from "./SlackWorkspaces"
import { SlackChannelList } from './SlackChannels'
import { configure } from "mobx";

// actionを経由せずに@observableをつけたプロパティを更新しようとするとエラーになるように設定
configure({ enforceActions: "always" });

export const slackWorkspaces = new SlackWorkspaceList();
export const slackChannels = new SlackChannelList();
