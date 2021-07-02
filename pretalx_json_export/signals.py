from django.dispatch import receiver

from pretalx.common.signals import register_data_exporters


@receiver(register_data_exporters, dispatch_uid="exporter_json_reviews")
def register_data_exporter(sender, **kwargs):
    from .exporter import ReviewExporter

    return ReviewExporter
