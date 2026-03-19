#!/usr/bin/bash

# Modules to test.
declare -ra test_modules=(enum)

########
# main #
########

for mod in ${test_modules[@]}; do
  micropython -m unittest $mod/*_test.py
done
