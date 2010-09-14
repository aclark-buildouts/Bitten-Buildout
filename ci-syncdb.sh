#!/bin/sh
bin/django --syncdb && echo OK || exit 1
