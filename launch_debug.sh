#!/usr/bin/env sh

nix-shell --run "VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/autorandr python3 $(realpath main.py)"
