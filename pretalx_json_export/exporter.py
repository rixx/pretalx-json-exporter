import json

from i18nfield.rest_framework import I18nAwareModelSerializer
from i18nfield.utils import I18nJSONEncoder
from pretalx.api.serializers.question import AnswerSerializer
from pretalx.api.serializers.submission import SubmissionSerializer
from pretalx.common.exporter import BaseExporter
from pretalx.submission.models import Review
from rest_framework import serializers


class ReviewSerializer(I18nAwareModelSerializer):
    submission = SubmissionSerializer()
    answers = AnswerSerializer(many=True)
    user = serializers.SlugRelatedField(slug_field="nick", read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "submission",
            "user",
            "text",
            "score",
            "override_vote",
            "created",
            "updated",
            "answers",
        )


class ReviewExporter(BaseExporter):
    identifier = "pretalx-json-exporter-reviews"
    verbose_name = "Reviews (JSON)"
    icon = "{ }"
    public = False
    cors = "*"

    def render(self, **kwargs):
        reviews = Review.objects.filter(submission__event=self.event)
        data = ReviewSerializer(reviews, many=True).data
        data = json.dumps(data, cls=I18nJSONEncoder)
        return f"{self.event.slug}-reviews.json", "application/json", data
