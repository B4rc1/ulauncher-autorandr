#!/usr/bin/env sh

ULAUNCHER_NIX_STORE_PATH=$(dirname $(dirname "$(readlink $(which ulauncher))"))

nix-shell --run "VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/autorandr PYTHONPATH="$ULAUNCHER_NIX_STORE_PATH/lib/python3.9/site-packages:$PYTHONPATH" python3 $(pwd)/main.py"
