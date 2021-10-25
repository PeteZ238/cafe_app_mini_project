#!/bin/bash
set -eu

if py -m pytest;
then
git add .
git commit
else
echo 'Tests have failed'
fi