# Docker Gitea

  * Gitea
  * https://docs.gitea.io/en-us/install-with-docker/
  * https://wiki.archlinux.org/index.php/Gitea#MariaDB/MySQL
  * themes for gitea?

Todo

## Cli

docker run -d --name test-gitea -p 8080:3000 -p 2221:22 -e DB_TYPE=mysql -e DB_NAME=gitea1 -e DB_USER=gitea -e DB_PASSWD=gitea -e DB_HOST=10.100.0.3:3306 gitea/gitea:latest
