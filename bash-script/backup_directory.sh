#!/bin/bash

timestamp=$(date +%Y_%m_%d)

CURRENT_DIR="dir1"
BACKUP_DIR="dir2"

tar -czf ${BACKUP_DIR}/backup_dir1_${timestamp}.tar.gz -C ${CURRENT_DIR} .
