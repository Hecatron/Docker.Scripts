#!/bin/bash

scriptsdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Backup databases
$scriptsdir/db-backup.sh
# Backup volumes
$scriptsdir/volume-backup.sh
# Copy backups to file server
$scriptsdir/copy-backups.sh
# Housekeep over 30 days
$scriptsdir/housekeep.sh

