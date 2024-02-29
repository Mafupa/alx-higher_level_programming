#!/usr/bin/env bash
# Sends a request to a URL
curl -s "$1" | wc -c
