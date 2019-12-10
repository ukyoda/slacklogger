
function env(name, defaultParameter) {
  if (typeof process.env[name] === 'undefined') {
    return defaultParameter
  } else {
    return process.env[name]
  }
}

module.exports = {
  db: {
    user: process.env.MYSQL_USER
  }
}