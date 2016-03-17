"""

    Geotrek startup script.

    This is executed only once at startup.

"""
from django.db.models.signals import pre_migrate, post_migrate
from django.conf import settings
from django.db import connection
from django.core.exceptions import ImproperlyConfigured

from mapentity.helpers import api_bbox
from django.core.management import call_command
from geotrek.common.utils.postgresql import load_sql_files, move_models_to_schemas


"""
    http://djangosnippets.org/snippets/2311/
    Ensure South will update our custom SQL during a call to `migrate`.
"""


def run_initial_sql_post_migrate(sender, **kwargs):
    app_label = kwargs.get('app_config').label
    load_sql_files(app_label)
    move_models_to_schemas(app_label)


def check_srid_has_meter_unit(sender, **kwargs):
    if not hasattr(check_srid_has_meter_unit, '_checked'):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM spatial_ref_sys
            WHERE srtext ILIKE '%%meter%%' AND srid=%s;""", [settings.SRID])
        results = cursor.fetchall()
        if len(results) == 0:
            err_msg = 'Unit of SRID EPSG:%s is not meter.' % settings.SRID
            raise ImproperlyConfigured(err_msg)
    check_srid_has_meter_unit._checked = True

pre_migrate.connect(check_srid_has_meter_unit, dispatch_uid="geotrek.core.checksrid")
post_migrate.connect(run_initial_sql_post_migrate, dispatch_uid="geotrek.core.sqlautoload")


"""
    Computed client-side setting.
"""
settings.LEAFLET_CONFIG['SPATIAL_EXTENT'] = api_bbox(settings.SPATIAL_EXTENT, buffer=settings.VIEWPORT_MARGIN)
