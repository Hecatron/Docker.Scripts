# NginxProxyManager

  * https://nginxproxymanager.com/


## Setup

To setup run
```
./setup.py
```


### Setup the Database

  * databaseid: webproxymgr
  * user: webproxymgr
  * pass: webproxymgr


### Login

  * http://app.gbd.local:9001 - devel
  * Login on install: admin@example.com / changeme


## Proxy Mappings

  * Set the default http landing page - http://app.gbd.local to the wiki with a list of sites on

  * http://app.gbd.local:9000 -> portainer devel
  * http://app.gbd.local:9100 -> portainer live
  * http://app.gbd.local:9101 -> web proxy manager

Proxied:

  * http://app.gbd.local -> proxy -> to wikijs / page list
  * http://git.gbd.local -> proxy -> gitea
  * http://wiki.gbd.local -> proxy -> wikijs
  * http://gbdwiki.gbd.local -> proxy -> dokuwiki (old)
  * http://webdev.gbd.local -> nginx host

## Todo

check that custom locations can be proxied
https://serverfault.com/questions/792326/nginx-proxy-pass-using-subfolder
