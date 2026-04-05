#!/usr/bin/bash

declare -ra deps=(unittest unittest-discover)

for dep in "${deps[@]}"; do
  micropython -m mip install "$dep"
done