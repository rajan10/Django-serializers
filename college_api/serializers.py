from rest_framework import serializers
class collegeSerializer(serializers.Serializer):
    # type(serializer.data['id'] <class 'int'>
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    location=serializers.CharField(max_length=50)
    phone=serializers.CharField()