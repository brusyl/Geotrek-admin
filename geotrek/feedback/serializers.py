from django.contrib.gis.geos import GEOSGeometry
from rest_framework import serializers as rest_serializers
from django.conf import settings
from geotrek.feedback import models as feedback_models


class ReportSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = feedback_models.Report
        geo_field = 'geom'
        id_field = 'id'

    def validate_geom(self, value):
        return GEOSGeometry(value, srid=settings.API_SRID)
