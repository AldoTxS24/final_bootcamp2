from django.test import TestCase
from django.utils import timezone
from movie.models import Movie, Genero

from django_dynamic_fixture import G, F

class MovieModelTestCase(TestCase):

    def setUp(self):
        self.genero = Genero.objects.create(name='Horror')
        self.movie = Movie.objects.create(
            name = 'Star Wars 4',
            rating = 8.50,
            genero = self.genero,
            created_date = timezone.now()
        )

        self.movie_g = G(Movie, genero=F(name='Test Genero'))

        self.qs_p = Movie.objects.all()

    def test_movie_str_method(self):
        print('*' * 20)
        print (self.qs_p)
        print('*' * 20)
        expected_str = f'{self.movie.name} | '
        self.assertEqual(str(self.movie), expected_str)
