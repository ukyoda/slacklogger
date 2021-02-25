import React from 'react'
import { observer } from 'mobx-react'
import { slackChannels } from '../store/store'

const View = observer(() => {
  console.log(slackChannels.state)
  if (slackChannels.state === 'done') {
    return (
      <pre>
        {JSON.stringify(slackChannels.channels, null, '    ')}
      </pre>
    )
  } else if (slackChannels.state === 'pending') {
    return <div>Wait...</div>
  } else {
    return <div>エラーが発生しました</div>
  }
})

export default observer(() => {
  
  return (
    <div>
      <View />
      <button onClick={() => slackChannels.fetch('TPZDE9NMP')}>更新</button>
    </div>
  );
})
