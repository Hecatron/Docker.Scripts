#!/bin/bash

volumeroot="/mnt/vol2/var/docker-prod/volumes"
volumedest="/mnt/vol2/var/backups/docker-prod-backup/volumes"

# Create directory for volume backups
mkdir -p $volumedest

echo "Backing up prod volumes"
tar -czvf ${volumedest}/live_gitea-$(date +\%F).tar.gz $volumeroot/live_gitea
tar -czvf ${volumedest}/live_mariadb-$(date +\%F).tar.gz $volumeroot/live_mariadb
tar -czvf ${volumedest}/live_webproxymgr-$(date +\%F).tar.gz $volumeroot/live_webproxymgr
tar -czvf ${volumedest}/live_wikijs-bch-$(date +\%F).tar.gz $volumeroot/live_wikijs-bch
tar -czvf ${volumedest}/live_wikijs-gbd-$(date +\%F).tar.gz $volumeroot/live_wikijs-gbd
tar -czvf ${volumedest}/portainer_data-$(date +\%F).tar.gz $volumeroot/portainer_data

echo "done"
