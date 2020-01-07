/**
 * Next.jsでは、_app.tsnが絶対に呼び出されるらしい。
 */
import React from 'react'
import App, { Container } from 'next/app'
import Head from 'next/head'
import "bootstrap/dist/css/bootstrap.min.css";

import { library } from '@fortawesome/fontawesome-svg-core'; //fontawesomeのコアファイル
import { fab } from '@fortawesome/free-brands-svg-icons'; //fontawesomeのbrandアイコンのインポート
import { fas } from '@fortawesome/free-solid-svg-icons'; //fontawesomeのsolidアイコンのインポート
import { far } from '@fortawesome/free-regular-svg-icons'; //fontawesomeのregularアイコンのインポート

library.add(fab, fas, far); //他のコンポーネントから簡単に呼び出せるようにするための登録処理？

type MyProps = {
  Component: any,
  router: any,
  ctx: any
};

export default class MyApp extends App {
  
  static async getInitialProps({ Component, ctx /*, router*/ }: MyProps) {
    let pageProps = {};

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx);
    }

    return { pageProps };
  }

  render() {
    const { Component, pageProps } = this.props;

    return (
      <Container>
        <Head>
          <title>Slackログびゅ〜あ</title>
          <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" cross-origin="anonymous"></link>
        </Head>
        <Component {...pageProps} />
      </Container>
    );
  }
}
