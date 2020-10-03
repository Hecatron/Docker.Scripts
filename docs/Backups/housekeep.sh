#!/bin/bash

# House keep any files older than 30 days
echo "Housekeeping backups"
find /mnt/vol2/var/backups/* -mtime +30 -exec rm {} \;

echo "done"
