#!/usr/bin/bash

shopt -s globstar; micropython -m unittest **/*_test.py

if [ $? != 0 ]; then
  echo
  echo "Some test has failed."
  exit $?
fi