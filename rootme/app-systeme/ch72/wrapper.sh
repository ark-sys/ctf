#!/bin/bash

ssh -q -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i .ssh/id_rsa app-systeme-ch72-crk@localhost

exit $?
