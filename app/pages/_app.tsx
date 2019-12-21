/**
 * Next.jsでは、_app.tsnが絶対に呼び出されるらしい。
 */
import React from 'react'
import App, { Container } from 'next/app'

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
        <Component {...pageProps} />
      </Container>
    );
  }
}
