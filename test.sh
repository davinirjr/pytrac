#!/bin/bash
docker build --force-rm -t pytrac/debian:stable .
docker run --rm -t -i -v $PWD:/home/pytrac/data pytrac/debian:stable
