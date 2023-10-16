#!/bin/bash

curl -o actions-runner-linux-x64-2.309.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.309.0/actions-runner-linux-x64-2.309.0.tar.gz
mkdir /users/lngo/csc231
mkdir /users/lngo/csc331
tar xzf ./actions-runner-linux-x64-2.309.0.tar.gz -C /users/lngo/csc231
tar xzf ./actions-runner-linux-x64-2.309.0.tar.gz -C /users/lngo/csc331
chown -R lngo: /users/lngo/csc231
chown -R lngo: /users/lngo/csc331
