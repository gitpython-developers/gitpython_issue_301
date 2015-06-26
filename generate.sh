#!/bin/bash

set -e
set -x

for i in {1..5000}; do
    git checkout -b "testcommit${i}"
    echo "commit $i" > testfile
    git add testfile
    git commit -m "commit ${i}"
    git checkout master
done
