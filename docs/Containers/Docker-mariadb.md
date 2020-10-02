# Docker MariaDb

  * https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/
  * https://hub.docker.com/r/arm64v8/mariadb/


## Setup

To setup run
```
./setup.py
```


### Client Tools

For the client tools on the host
```
# install client tools
emerge dev-db/mariadb

# To connect on port 3306 (3307 is for external)
mysql -u root -h 10.101.0.100 -p
```

For a gui client see sqlyog

  * https://github.com/webyog/sqlyog-community/wiki/Downloads


## To setup a new database

Under sqlyog first lets create a new database

  * right click the top level
  * select Create Database
  * name it something like gitea1

To create a user for the database

  * click the user manager icon in the toolbar
  * click add new user
  * enter in username / password
  * leave host as % for any host
  * select the database and grant all privileges
