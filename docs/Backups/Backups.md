# Backups

  * https://www.linode.com/docs/databases/mysql/use-mysqldump-to-back-up-mysql-or-mariadb/
  * https://github.com/blacklabelops/volumerize

## Backup scripts

path for backup scripts is /mnt/vol2/var/scripts/

  * **backup-all.sh** - example run all backup tasks
  * **housekeep.sh** - example script for housekeeping files to 30 days
  * **volume-backup.sh** - example script for backing up docker volumes as .tar.gz files

### Mysql / mariadb backups

  * **db-backup.sh** - example script for backing up mariadb databases

Place the database credentials ito a seperate file <br>
example:

**db-backup.cnf**
```
[client]
user = root
password = rootpass
```

Make sure other users cannot read it
```
chmod o-r db-backup.cnf
```

### rsync copy script

  * **copy-backups.sh** - example script for copying across to an rsync destination

Place the rsync password into a seperate file <br>
This should just be the file on it's own - **rsync.cnf**

Make sure other users cannot read it
```
chmod o-r rsync.cnf
```

### Cronjob

  * https://crontab.guru/every-day-at-1am

To setup a cron job to run the backup script every morning at 1am <br>
add the following to /etc/crontab
```
# add the following to /etc/crontab
0 1 * * *  root  /mnt/vol2/var/scripts/backup-all.sh
```

Next reload the crontab
```
# reload crontab
crontab /etc/crontab
```
