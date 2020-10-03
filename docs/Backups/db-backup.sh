#!/bin/bash

# Create directory for database backups
mkdir -p /mnt/vol2/var/backups/docker-prod-backup/mariadb/

dumpconf="/mnt/vol2/var/scripts/db-backup.cnf"
dumpconn="-u root -h 127.0.0.1 --port=3307"
dumpopts="--defaults-extra-file=$dumpconf $dumpconn --single-transaction --quick --lock-tables=false"
dumpdest="/mnt/vol2/var/backups/docker-prod-backup/mariadb"

echo "Backing up gitea database"
mysqldump $dumpopts --databases gitea > $dumpdest/full-backup-gitea-$(date +\%F).sql

echo "Backing up webproxymgr database"
mysqldump $dumpopts --databases webproxymgr > $dumpdest/full-backup-webproxymgr-$(date +\%F).sql

echo "Backing up wikijs-gbd database"
mysqldump $dumpopts --databases wikijs-gbd > $dumpdest/full-backup-wikijs-gbd-$(date +\%F).sql

echo "Backing up wikijs-bch database"
mysqldump $dumpopts --databases wikijs-bch > $dumpdest/full-backup-wikijs-bch-$(date +\%F).sql

echo "done"

