from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models

from test_auditlog.models import AuditAbstractModel

class Poll(AuditAbstractModel):
    """Model with history field"""
    # If pk is not numeric set pk_indexable to false
    history = AuditlogHistoryField()
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(AuditAbstractModel):
    """Model without history field"""
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# Register model for log
auditlog.register(Poll, serialize_data=True) # serialize include the current object
auditlog.register(Choice)
