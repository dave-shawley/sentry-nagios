from sentry.plugins import Plugin


VERSION = '1'


class SentryNagios(Plugin):
    title = 'Sentry Nagios'
    slug = 'nagios'
    description = 'Alert: sent to Nagios'
    version = VERSION
    author = 'Dave Shawley'
    author_url = 'https://github.com/dave-shawley/sentry_nagios'
