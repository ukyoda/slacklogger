import React from 'react'
import { useRouter } from "next/router";
import ChannelList from '../../../components/channelList'
import Layout from '../../../components/layouts/default'

export default () => {
  const router = useRouter();
  const { wsid } = router.query
  return (
    <Layout>
      <ChannelList wsid={wsid as string} />
    </Layout>
  );
}
