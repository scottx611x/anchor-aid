#!/usr/bin/env bash
jq -n --arg name $(jq --raw-output .production.project_name ../zappa_settings.json) '{"name": $name}'