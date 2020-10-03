# NginxProxyManager

  * https://nginxproxymanager.com/


## Setup


### Setup the Database

  * databaseid: webproxymgr
  * user: webproxymgr
  * pass: webproxymgr


### Script

To setup run
```
./setup.py
```


### Login

  * http://app.gbd.local:9001 - devel
  * Login on install: admin@example.com / changeme


## Proxy Mappings

### Development

  * http://app.gbd.local:9000 -> portainer devel

### Live


  * http://app.gbd.local -> Set the default http landing page to the wiki with a list of sites on
    ports 80 / 443

  * http://app.gbd.local:9100 -> portainer live
  * http://app.gbd.local:9101 -> web proxy manager admin
  * http://app.gbd.local:9102 -> web proxy manager api
  * http://app.gbd.local:9103 -> gitea web
  * http://app.gbd.local:222 -> gitea ssh



### Proxied

  * http://app.gbd.local -> proxy -> to wikijs / page list
  * http://git.gbd.local -> proxy -> gitea
  * http://wiki.gbd.local -> proxy -> wikijs
  * http://gbdwiki.gbd.local -> proxy -> dokuwiki (old)
  * http://webdev.gbd.local -> nginx host

## Todo

check that custom locations can be proxied
https://serverfault.com/questions/792326/nginx-proxy-pass-using-subfolder
