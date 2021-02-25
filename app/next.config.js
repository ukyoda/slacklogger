const withCSS = require('@zeit/next-css')
const compose = require('next-compose')
module.exports = compose([
  [withCSS],
  {}
])
