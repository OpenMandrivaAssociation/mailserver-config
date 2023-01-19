#!/bin/sh
exec /usr/bin/rspamc -h /run/rspamd/worker-controller.socket learn_ham
