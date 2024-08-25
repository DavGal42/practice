#!/bin/bash

DEST_DIR=~/tmp/

find $DEST_DIR -type f -mtime +7 -exec rm {} \;
