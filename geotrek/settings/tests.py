from .default import *  # NOQA

#
#  Django Tests
# ..........................

TEST = True

TEST_EXCLUDE = ('django', 'mapentity')

LOGGING['handlers']['console']['level'] = 'CRITICAL'

LANGUAGE_CODE = 'en'

MAPENTITY_CONFIG['MAPENTITY_WEASYPRINT'] = False

MAILALERTSUBJECT = "Acknowledgment of feedback email"
