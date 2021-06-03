#!/bin/bash

uwsgi --master \
--https localhost:8080,\
certificates/site_public_key.pem,\
certificates/site_private_key.pem \
--mount /=demo_server:app
