import next from 'next'
const express = require('express')
const host = process.env.HOST || '0.0.0.0'
const port = parseInt(process.env.PORT || '3000', 10)
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()
const proxy = require("express-http-proxy");

app.prepare().then(() => {
  const server = express()
  // WebAPIのリバースプロキシ
  server.use('/api/v1/slack', 
    proxy("slackapi:3030", {
      proxyReqPathResolver (req: any) {
        return '/api/v1/slack' + req.url
      }
    })
  )
  // それ以外
  server.get('*', (req: any, res: any) => {
    return handle(req, res)
  })
  server.listen(port, host, (err: any) => {
    if (err) throw err
    console.log(`> Ready on ${process.env.CLIENT_URL || `http://${host}:${port}`}`)
  })

})
