from rest_framework import serializers
from datetime import datetime

class StudentSerializer(serializers.Serializer):
    roll_no=serializers.CharField(max_length=20)
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    # serializer.data['age']  <class 'int'>
    age=serializers.IntegerField()
    # serializer.data['created_at'] <class 'str'>
    created_at=serializers.DateTimeField()