#!/bin/bash


curl -s https://ipvigilante.com/$1 | jq '.data.city_name, .data.subdivision_1_name, .data.country_name'
