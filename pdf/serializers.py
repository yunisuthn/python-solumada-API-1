from django.db import models
from rest_framework import serializers
from pdf.models import myuploadfile

class MyUploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = myuploadfile
        fields = ('myfiles')