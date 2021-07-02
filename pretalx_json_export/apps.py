from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = 'pretalx_json_export'
    verbose_name = 'More JSON exports for pretalx'

    class PretalxPluginMeta:
        name = gettext_lazy('More JSON exports for pretalx')
        author = 'Tobias Kunze'
        description = gettext_lazy(
            'A range of additional JSON exports (questions, reviews, …)'
        )
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA
