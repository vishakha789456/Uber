from rest_framework import serializers
from users.models import *
class StudentsSerializers(serializers.ModelSerializers):
    class Meta:
        model=Students
        fields=('__all__')