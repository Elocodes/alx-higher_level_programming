#!/bin/bash
# cript sends request to url passed as arg, displays size in bytes of response
curl -s "$1" | wc -c
