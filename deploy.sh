#!/bin/sh

# -e exit on fail
# -u unset variables fail
# -x print commands to stdout
set -eux

cd ../cloud_drive

# Get dependencies and build release. `rel/config.exs` has build settings.
yes | mix deps.get
yes | mix release --env=prod --no-tar

# Start the server daemon as 'cloud-drive' user. Use `bin/cloud_drive remote_console`
# to connect to the server's shell.
sudo -u cloud-drive _build/prod/rel/cloud_drive/bin/cloud_drive start