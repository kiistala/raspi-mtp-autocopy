#!/bin/bash

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

SOURCEDIR="/media/SamsungTab3"
# sudo mkdir -p $SOURCEDIR

DESTDIR="/media/BackupMedia/$TIMESTAMP"
mkdir -p $DESTDIR

mtpfs -o allow_other $SOURCEDIR && cp -v $SOURCEDIR/*csv $DESTDIR/ && fusermount -u $SOURCEDIR && echo "OK"

