# todo

## Case

  * 3d printed case
  * 3d print cover for usb board

## General

  * ntp time on host
  * backups

## docker-prod
  
  * nginx proxy - setup
  * gitea - data transfer
  * wikijs - data transfer / git link
  * dokuwiki

## Host

  * nginx setup
    php / dotnet c# sites

## Hard disk

disk monitoring?
smartctl -a /dev/sdb
smartctl -H /dev/sdb
https://www.howtoforge.com/tutorial/monitor-harddisk-with-smartmon-on-ubuntu/
https://gist.github.com/te-online/37fc034c28fff38963b6cdbead5e8622


## Dns

  * https://stackoverflow.com/questions/41400603/dockers-embedded-dns-on-the-default-bridged-network
  * https://docs.docker.com/config/containers/container-networking/#ip-address-and-hostname



todo

  * dns between docker daemons?
  * dns from the outside?
  * https://medium.com/@huynhquangthao/how-does-the-docker-dns-work-ab69bde4c82a
  * https://stackoverflow.com/questions/52146056/how-to-delete-disable-docker0-bridge-on-docker-startup
  * https://hub.packtpub.com/container-linking-and-docker-dns/


docker -H unix:///var/run/docker-prod.sock run -it -d --name=test3 --restart=always --network=defnet-prod ubuntu:latest
docker attach




## embedded docker dns

  * https://stackoverflow.com/questions/39729663/query-docker-embedded-dns-from-host
  * https://github.com/phensley/docker-dns

docker run -d --name dns-test --network=defnet -v /var/run/docker.sock:/docker.sock phensley/docker-dns --domain example.com

docker logs dns-test


# Building docker images

note alpine:latest seems like a good basis for python apps
only 5Mb in size

docker build --network=defnet  https://github.com/phensley/docker-dns.git

docker run -d --name dns-test --network=defnet -v /var/run/docker.sock:/docker.sock f637f7306e28 --domain example.com

doesnt work

try this instead

docker run -d --name dns-test --network=defnet -v /var/run/docker.sock:/var/run/docker.sock -v /etc/resolv.conf:/etc/resolv.conf defreitas/dns-proxy-server:2.19.0-arm8x64

nope, use fixed ips instead


emerge dev-python/docker-py






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
  * http://app.gbd.local:9104 -> wikijs-gbd
  * http://app.gbd.local:9105 -> wikijs-bch


### Proxied

  * http://app.gbd.local -> proxy -> to wikijs / page list
  * http://wiki.gbd.local -> proxy -> wikijs
  * http://wikibch.gbd.local -> proxy -> wikijs


  * http://git.gbd.local -> proxy -> gitea
  * http://gbdwiki.gbd.local -> proxy -> dokuwiki (old)
  * http://webdev.gbd.local -> nginx host

## Todo

check that custom locations can be proxied
https://serverfault.com/questions/792326/nginx-proxy-pass-using-subfolder
