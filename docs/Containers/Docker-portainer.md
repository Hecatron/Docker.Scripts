# Docker Portainer

  * https://www.portainer.io/
  * https://appfleet.com/blog/top-gui-for-docker/


## Setup

To setup portainer from the command line


### For development

```
docker run -d -p 8000:8000 -p 9000:9000 \
  --name=portainer --restart=always --network=defnet \
  -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

### For live

```
docker -H unix:///var/run/docker-prod.sock run -d -p 8100:8000 -p 9100:9000 \
  --name=portainer --restart=always --network=defnet-prod \
  -v /var/run/docker-prod.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```
