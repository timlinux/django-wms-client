# coding=utf-8
import os
import sys
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'wms_client.tests.test_settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

from django.test.utils import get_runner
from django.conf import settings


def run():
    """Run the unittests."""
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['wms_client'])
    sys.exit(bool(failures))
