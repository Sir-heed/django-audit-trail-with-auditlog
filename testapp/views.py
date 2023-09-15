from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from auditlog.models import LogEntry

from . import models, serializers

class PollViewSet(ModelViewSet):
    model = models.Poll
    queryset = models.Poll.objects.filter(is_active=True)
    serializer_class = serializers.PollSerializer


class ChoiceViewSet(ModelViewSet):
    model = models.Choice
    queryset = models.Choice.objects.filter(is_active=True)
    serializer_class = serializers.ChoiceSerializer

    @action(
        methods=['GET'],
        detail=True,
        url_path='history',
        serializer_class=None,
    )
    def choice_history(self, request, pk=None):
        """Log does not maintain relationship with object but it stores
        object repr. as `object_repr`"""
        object = self.get_object()
        histories = LogEntry.objects.filter(object_repr=object.__str__())
        return Response(serializers.LogEntrySerializer(histories, many=True).data)


class LogEntryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = LogEntry
    queryset = LogEntry.objects.all()
    serializer_class = serializers.LogEntrySerializer
