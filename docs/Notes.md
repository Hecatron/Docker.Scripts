# Notes

## Python libs

I've found useful python library for talking to the docker api, is the docker python library. <br>
This seems to be the most recent one under gentoo.

```
emerge dev-python/docker-py
```

## Building docker images

alpine:latest seems like a good basis for python apps
only 5Mb in size


## Dns

When using user networks (not the default bridge one) <br>
You get dns resolution for free between containers via docker's embedded dns service <br>
(which I think shows up as 127.0.0.11 under resolve.conf in the docker containers)

However to handle dns between docker daemons or from the outside would require a dns proxy container of some form <br>
As a quick workaround to get around this, we can use fixed ip's

### Links

  * https://stackoverflow.com/questions/41400603/dockers-embedded-dns-on-the-default-bridged-network
  * https://docs.docker.com/config/containers/container-networking/#ip-address-and-hostname
  * https://medium.com/@huynhquangthao/how-does-the-docker-dns-work-ab69bde4c82a
  * https://stackoverflow.com/questions/52146056/how-to-delete-disable-docker0-bridge-on-docker-startup
  * https://hub.packtpub.com/container-linking-and-docker-dns/
  * https://stackoverflow.com/questions/39729663/query-docker-embedded-dns-from-host
  * https://github.com/phensley/docker-dns
