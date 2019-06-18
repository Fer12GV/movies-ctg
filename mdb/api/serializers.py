from django.urls import reverse
from rest_framework import serializers

from mdb.models import MovieRate


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    release_date = serializers.DateField(input_formats=['%d/%m/%Y'])
    duration = serializers.IntegerField()
    rate = serializers.SerializerMethodField(method_name='get_movie_rate')

    def get_movie_rate(self, obj):
        rates = MovieRate.objects.get_rate_for_movie(obj)
        if rates.exists():
            return rates.first()['rate']

        return ''


class MovieRateSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id')
    id = serializers.HyperlinkedIdentityField(view_name='api-mdb:movie-detail-actions')
    user = serializers.StringRelatedField()
    movie_link = serializers.HyperlinkedRelatedField(source='movie', read_only=True,
                                                     view_name='drf-movie-detail',
                                                     lookup_field='slug')
    movie = MovieSerializer()

    class Meta:
        model = MovieRate
        fields = ('movie', 'user', 'rate', 'id', 'movie_link', 'pk')