from geotrek.common.models import Theme
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(Theme)
class ThemeTO(TranslationOptions):
    fields = ('label', )
