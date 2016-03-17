from .default import *  # NOQA

#
#  Django Tests
# ..........................

TEST = True

TEST_EXCLUDE = ('django',)

LOGGING['handlers']['console']['level'] = 'CRITICAL'

LANGUAGE_CODE = 'en'

MAPENTITY_CONFIG['MAPENTITY_WEASYPRINT'] = True
