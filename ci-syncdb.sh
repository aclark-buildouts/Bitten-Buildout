#!/bin/sh
bin/django syncdb --migrate && echo OK || exit 1
