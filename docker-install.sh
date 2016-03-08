#!/usr/bin/env bash

./install.sh --noinput
make load_data
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | ./bin/django shell
supervisorctl stop all
