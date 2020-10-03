#!/bin/bash

# Backup databases
./db-backup.sh
# Backup volumes
./volume-backup.sh
# Copy backups to file server
./copy-backups.sh
# Housekeep over 30 days
./housekeep.sh

