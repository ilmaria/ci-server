#!/bin/sh

cd ../cloud_drive

yes | mix deps.get
yes | mix release --env=prod --no-tar

sudo -u cloud-drive _build/prod/rel/cloud_drive/bin/cloud_drive start