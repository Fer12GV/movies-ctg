from rest_framework import serializers

"""class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'"""


class Movieserializer(serializers.ModelSerializer):
    title = serializers.CharField()
    release_date = serializers.DateField(input_formats=['%d/%m/%Y'])
    duration = serializers.IntergerField()
    rate = serializers.FloatField(default=5)
