import unittest

from hamcrest import assert_that, equal_to
import sentry.plugins

from tests.matchers import subclass_of
import sentry_nagios


class SentryPluginRequirementsTest(unittest.TestCase):
    # see http://sentry.readthedocs.org/en/latest/developer/plugins/

    def test_that_version_is_set(self):
        assert_that(sentry_nagios.VERSION, equal_to('1'))

    def test_that_plugin_has_title(self):
        assert_that(sentry_nagios.SentryNagios.title,
                    equal_to('Sentry Nagios'))

    def test_that_plugin_has_slug(self):
        assert_that(sentry_nagios.SentryNagios.slug, equal_to('nagios'))

    def test_that_plugin_has_description(self):
        assert_that(sentry_nagios.SentryNagios.description,
                    equal_to('Alert: sent to Nagios'))

    def test_that_plugin_has_version(self):
        assert_that(sentry_nagios.SentryNagios.version,
                    equal_to(sentry_nagios.VERSION))

    def test_that_plugin_has_author(self):
        assert_that(sentry_nagios.SentryNagios.author,
                    equal_to('Dave Shawley'))

    def test_that_plugin_has_author_url(self):
        assert_that(sentry_nagios.SentryNagios.author_url,
                    equal_to('https://github.com/dave-shawley/sentry_nagios'))

    def test_that_plugin_implements_required_interface(self):
        assert_that(sentry_nagios.SentryNagios,
                    subclass_of(sentry.plugins.Plugin))
