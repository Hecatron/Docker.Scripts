# Docker Gitea

  * https://docs.gitea.io/en-us/install-with-docker/
  * https://wiki.archlinux.org/index.php/Gitea#MariaDB/MySQL
  * https://gitea.com/gitea/awesome-gitea


## Setup


### Setup the Database

  * databaseid: gitea
  * user: gitea
  * pass: gitea


### Host User

gitea will setup its own user called "git" inside docker
so we don't need to worry about it / just leave it as the default user id of git


### Script

To setup run
```
./setup.py
```


### Themes

```
# first lets create a directory for the themes
cd /mnt/vol2/var/docker-prod/volumes/live_gitea/_data/gitea/
mkdir -p themes
cd themes

# Next lets clone them all
git clone https://gitea.artixlinux.org/artix/gitea-dark-blue.git
git clone https://github.com/TylerByte666/gitea-matrix-template.git
git clone https://github.com/Th3Whit3Wolf/Space-Gitea.git
git clone https://github.com/iamdoubz/Gitea-Dark-Red-Theme.git
```

Since some themes use custom template overlays
I've found the best way is to just use symlinks

```
cd /mnt/vol2/var/docker/volumes/devel_gitea/_data/gitea/
chown -R 1000:1000 themes
ln -s themes/gitea-matrix-template/templates templates
ln -s themes/gitea-matrix-template/public public
chown -R 1000:1000 public templates
```

Then edit the **conf/app.ini** file and set the theme name here
```
[ui]
THEMES = gitea,arc-green,matrix
DEFAULT_THEME = matrix
```

Under the server section set the the domains and root url
```
[server]
APP_DATA_PATH    = /data/gitea
DOMAIN           = app.gbd.local
SSH_DOMAIN       = app.gbd.local
HTTP_PORT        = 3000
ROOT_URL         = http://app.gbd.local:3000
```

Followed by a gitea restart


todo setup live with webproxy and old data
http://app.gbd.local:4000/
