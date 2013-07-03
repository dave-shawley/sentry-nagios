#!/usr/bin/env python
#

import os

import nose


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'sentry.conf.defaults'
    nose.run()
