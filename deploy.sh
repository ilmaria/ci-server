#!/bin/sh

# -e exit on fail
# -u unset variables fail
# -x print commands to stdout
set -eux

cd ../cloud_drive

# Echo yes to interactive questions. `rel/config.exs` has release build settings.
echo "y\ny\ny\n" | mix deps.get
echo "y\ny\ny\n" | MIX_ENV=prod mix release --env=prod --no-tar

# Allow 'cloud-drive' user to modify this file. The 'cloud_drive' executable
# will want to modify this.
chmod -R o+w _build/prod/rel/cloud_drive/releases/start_erl.data

# Start the server daemon as 'cloud-drive' user. Use `bin/cloud_drive remote_console`
# to connect to the server's shell.
sudo -u cloud-drive _build/prod/rel/cloud_drive/bin/cloud_drive start