#!/bin/bash

# Copy across the data from the backups folder to the file server
echo "Copying backups to file server"
rsync --password-file=/mnt/vol2/var/scripts/rsync.cnf -av /mnt/vol2/var/backups appservbackup@bigal.gbd.local::backups/app-server/

echo "done"

