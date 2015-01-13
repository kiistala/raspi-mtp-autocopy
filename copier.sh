#!/bin/bash

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
DATESTAMP=$(date +%Y%m%d)

SOURCEDIR="/media/SamsungTab3"
fusermount -u $SOURCEDIR
wait

DESTDIR="/media/usb/$TIMESTAMP"
sudo mkdir -p -v $DESTDIR

BACKUPDIR_ON_RASPI="/home/pi/rsynced/$DATESTAMP"

# rsync $SOURCEDIR/*csv $BACKUPDIR_ON_RASPI/

mtpfs -o allow_other -o nonempty $SOURCEDIR && cp -v $SOURCEDIR/*csv $DESTDIR/ && fusermount -u $SOURCEDIR

# mtpfs -o allow_other $SOURCEDIR && cp -v $SOURCEDIR/*csv $DESTDIR/ && fusermount -u $SOURCEDIR && echo "OK"

