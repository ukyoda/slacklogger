import React from 'react'
import Link from 'next/link'
import Layout from '../components/layouts/default'
import SlackAPI from '../libs/SlackAPI'

export default () => {
  const api = new SlackAPI()
  api.workspaces()
      .then((res: any) => console.log(res))
      .catch((err: any) => console.error(err))
  return (
    <Layout>
      <ul>
        <li>
          <Link href="/a" as="/a">
            <a>a</a>
          </Link>
        </li>
        <li>
          <Link href="/b" as="/b">
            <a>b</a>
          </Link>
        </li>
      </ul>
    </Layout>
  );

}
