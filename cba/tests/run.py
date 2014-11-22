#!/usr/bin/env python
import sys

import dj_database_url
import django
from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings
from django.test.runner import DiscoverRunner


settings.configure(
    DATABASES={'default': dj_database_url.config(
        default='postgres://localhost/cba',
    )},
    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    INSTALLED_APPS=(
        'cba',

        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
    ),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher',),
    SITE_ID=1,
    ROOT_URLCONF='cba.tests.urls',
    MIDDLEWARE_CLASSES=(),
)


django.setup()


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    """Enable coloured output for tests."""


test_runner = TestRunner(verbosity=1)
failures = test_runner.run_tests(['cba'])
if failures:
    sys.exit(1)
