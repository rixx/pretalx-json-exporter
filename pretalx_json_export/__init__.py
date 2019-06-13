from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretalx_json_export'
    verbose_name = 'More JSON exports for pretalx'

    class PretalxPluginMeta:
        name = ugettext_lazy('More JSON exports for pretalx')
        author = 'Tobias Kunze'
        description = ugettext_lazy(
            'A range of additional JSON exports (questions, reviews, …)'
        )
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretalx_json_export.PluginApp'
