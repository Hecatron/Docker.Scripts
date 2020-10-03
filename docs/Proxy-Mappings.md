# Proxy Mappings

## Development

  * http://app.gbd.local:9000 -> portainer devel

## Live

  * http://app.gbd.local -> Set the default http landing page to the wiki with a list of sites on
    ports 80 / 443

  * http://app.gbd.local:9100 -> portainer live
  * http://app.gbd.local:9101 -> web proxy manager admin
  * http://app.gbd.local:9102 -> web proxy manager api
  * http://app.gbd.local:9103 -> gitea web
  * http://app.gbd.local:222 -> gitea ssh
  * http://app.gbd.local:9104 -> wikijs-gbd
  * http://app.gbd.local:9105 -> wikijs-bch


### Proxied

  * http://app.gbd.local -> proxy -> to wikijs / page list
  * http://wiki.gbd.local -> proxy -> wikijs
  * http://wikibch.gbd.local -> proxy -> wikijs


  * http://git.gbd.local -> proxy -> gitea
  * http://gbdwiki.gbd.local -> proxy -> dokuwiki (old)
  * http://webdev.gbd.local -> nginx host
