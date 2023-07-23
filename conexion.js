const pymysql = require("pymysql");

// Establish the connection
const conn = pymysql.connect({
  host: "localhost",
  port: 3306,
  user: "root",
  password: "12345",
  database: "luna_baby",
});

// Export the connection
module.exports = conn;
