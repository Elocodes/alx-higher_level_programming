#!/usr/bin/bash
# script sends in a header variable and its value, and displays response
curl -sL -H "X-School-User-Id: 98" "$1"
