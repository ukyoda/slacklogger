/**
 * Next.jsでは、_app.tsnが絶対に呼び出されるらしい。
 */
import React from 'react'
import App from 'next/app'
import Head from 'next/head'
import "bootstrap/dist/css/bootstrap.min.css";

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
      <div>
        <Head>
          <title>Slackログびゅ〜あ</title>
          <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossOrigin="anonymous"></link>
        </Head>
        <Component {...pageProps} />
      </div>
    );
  }
}
