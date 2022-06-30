#!/usr/bin/env bash

sudo /home/guoc/.pyenv/versions/soil-sensor/bin/gunicorn -w 1 -b 0.0.0.0 'app:app'
