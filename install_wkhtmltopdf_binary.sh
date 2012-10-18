#!/bin/bash

if [ "`uname -m`" = "x86_64" ] ; then
    ARCH="amd64"
else
    ARCH="i386"
fi
BIN=/usr/bin/wkhtmltopdf

if [ -f $BIN ] ; then
    echo "$BIN already exists"
    exit 1
fi

set -e

wget -q http://wkhtmltopdf.googlecode.com/files/wkhtmltopdf-0.11.0_rc1-static-$ARCH.tar.bz2 -O- | \
sudo tar -xjf - -C /tmp
sudo mv /tmp/wkhtmltopdf-$ARCH $BIN
sudo chmod 755 $BIN
sudo chown root:root $BIN
