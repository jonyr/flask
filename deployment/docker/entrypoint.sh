#!/bin/bash
set -e

if [[ $1 == 'api' ]] ; then
  gunicorn -c ./src/config/gunicorn.py wsgi:app
  exit 0
fi

exec "$@"
