#!/usr/bin/bash

shopt -s globstar; micropython -m unittest **/*_test.py
