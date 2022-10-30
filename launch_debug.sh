#!/usr/bin/env sh

nix-shell --run "VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/autorandr PYTHONPATH="/nix/store/3asq37jnzdm7cya2q0wz54p6ms9zns5d-ulauncher-5.15.0/lib/python3.9/site-packages:$PYTHONPATH" python3 main.py"
