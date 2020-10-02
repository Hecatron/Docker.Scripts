# Docker dokuwiki

  * https://hub.docker.com/r/linuxserver/dokuwiki

Todo


```
---
version: "2.1"
services:
  dokuwiki:
    image: linuxserver/dokuwiki
    container_name: dokuwiki
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/appdata/config:/config
    ports:
      - 80:80
      - 443:443 #optional
    restart: unless-stopped
```
