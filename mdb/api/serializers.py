from rest_framework import serializers

from mdb.models import MovieRate, Movie

class MovieSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id')
    poster = serializers.ImageField(read_only=True)
    trailer_url = serializers.URLField(required=False)
    class Meta:
        model = Movie
        fields = ('title',
                  'duration',
                  'poster',
                  'detail',
                  'trailer_url',
                  'genre',
                  'original_language',
                  'country',
                  'release_date', 'pk')


class MovieRateSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id', read_only=True)
    #id = serializers.HyperlinkedIdentityField(view_name='api-mdb:movierate-detail-actions')
    user = serializers.StringRelatedField()
    #movie_link = serializers.HyperlinkedRelatedField(source='movie', read_only=True,
    #                                                 view_name='api-mdb:movie-detail-actions')
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieRate
        fields = ('movie', 'user', 'pk', 'rate')
        #fields = ('movie', 'user', 'rate', 'id', 'movie_link', 'pk')