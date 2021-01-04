/*******************************************************************************
 *  © 2007-2019 - LogicMonitor, Inc. All rights reserved.
 ******************************************************************************/

import groovy.sql.Sql

// set host variables.
def hostname = hostProps.get("system.hostname")
def user = hostProps.get("jdbc.mysql.user")
def pass = hostProps.get("jdbc.mysql.pass")
def port = (hostProps.get("jdbc.mysql.port") ? hostProps.get("jdbc.mysql.port").toInteger() : 3306)

// construct the URL.
def url = "jdbc:mysql://" + hostname + ":" + port

// MariaDB driver (works for both MariaDB & MySQL)
def driver = "org.mariadb.jdbc.Driver"

// Create a connection to the SQL server
sql = Sql.newInstance(url, user, pass, driver)

// Iterate over query results and list the databases
sql.eachRow('select host, user from mysql.user;') {
    println(it.User + "@" + it.Host + "##" + it.User + "@" + it.Host + "####host=" + it.Host)
}

// Close the connection
sql.close()

return 0