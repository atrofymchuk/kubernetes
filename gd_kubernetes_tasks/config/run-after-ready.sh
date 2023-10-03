#!/bin/sh
curl -X PUT "localhost:9200/elastic" -H 'Content-Type: application/json' -d'{ "settings" : { "index" : { } }}'