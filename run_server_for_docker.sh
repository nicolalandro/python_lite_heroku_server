#!/usr/bin/env bash
export pcloud_uname=<YOUR CLOUD UNAME>
export pcloud_password=<YOUR CLOUD PASSWORD>
gunicorn -b 0.0.0.0:5000 main:app --log-file=-