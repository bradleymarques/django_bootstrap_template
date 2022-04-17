# Django Python Template

## What's included

+ A dev container
+ Poetry
+ Black
+ Docker Image
+ Code coverage with automatic posting to GitHub PRs
+ Some wicked git hooks
+ Some useful shortcuts

## Settings

There are multiple Django settings files for different needs:

+ `base_settings.py` - this runs a sqlite server and is useful for fast local development and CI
  + `postgres_settings.py` - inherits from `base_settings.py` and runs a PostgreSQL database. Useful for a live environment such as a staging server or even a production server
