#!/bin/sh

rm -fr ATBI_files Geojsons
. /usr/share/modules/init/bash
module load python/2.7
export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH
python separate.py ATBI_records.csv

