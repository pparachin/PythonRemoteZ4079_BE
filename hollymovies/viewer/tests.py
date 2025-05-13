from platform import release

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from .models import Genre, Actor, Director, Movie

"""
class ModelsTest(TestCase):
    "Vytvoření instancí tříd modelů"
    def setUp(self):
        self.genre = Genre.objects.create(name="Horror", description="Strašidelné filmy")
        self.actor = Actor.objects.create(name="Will", surname="Smith", birth_day="1976-3-2")
        self.actor2 = Actor.objects.create(name="Wil", surname="Smth", birth_day="1972-3-2")
        self.director = Director.objects.create(name="Quentin", surname="Tarantino", birth_day="1963-03-27")
        self.movie = Movie.objects.create(
            title = "Pulp Fiction: Historky z podsvětí",
            genre = self.genre,
            rating = 10,
            released = 1994,
            description = "Nejkultovnější z kultovních filmů 90. let je autorskou Biblí Quentina Tarantina, který v tomto opusu definoval základní prvky své režisérské poetiky a vytvořil dílo rozněcující náročné kritiky na festivalu v Cannes, levicové a pravicové intelektuály i zedníky dopřávající si po těžké šichtě trochu oddychu. Pulp Fiction je multižánrovým opusem, který přetéká fetišistickými detaily a popkulturními odkazy a zároveň dokonale funguje jako svrchovaně napínavý film rozvržený do inovativní příběhové struktury. Chcete vidět homosexuální znásilnění sbližující dva nepřátele na život a na smrt?",
            director = self.director
        )
        self.movie.actor.add(self.actor)
        self.movie.actor.add(self.actor2)

    def test_genre(self):
        self.assertEqual(str(self.genre), "Horror")

    def test_actor_str(self):
        self.assertEqual(str(self.actor), "Will Smith")

    def test_director_str(self):
        self.assertEqual(str(self.director), "Quentin Tarantino")

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Pulp Fiction: Historky z podsvětí (1994)")

    def test_movie_actor(self):
        print(self.movie.actor.all())
        print(self.actor)
        "Zvážit možnost použití cyklu k projetí všech herců i filmu"
        self.assertIn(str(self.actor), str(self.movie.actor.all()))


    "Úkol: vytvořit to stejné pro film"
    "Přidat k filmu herce"
"""

class ActorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.actor = Actor.objects.create(
            name="Matthew", surname="Perry", birth_day="1969-08-19", image_url="actors/2025/04/28/ /162421110_404a88.jpg"
        )
        self.url_list = reverse("actors")
        #self.url_detail = reverse("actor_detail", args=[self.actor.pk])
        self.url_detail = f"/cs/actor/{self.actor.pk}/"

    def test_actor_list(self):
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "actors/index.html")
        self.assertIn(self.actor, resp.context["object_list"])

    def test_actor_detail_permission_denied(self):
        user = User.objects.create_user(username="tester", password="pass")
        self.client.login(username="tester", password="pass")
        resp = self.client.get(self.url_detail)
        print(self.url_detail)
        self.assertNotEqual(resp.status_code, 200)
        print(resp.status_code)
        self.assertIn(resp.status_code, (403, 302))

    def test_actor_detail_with_permission(self):
        user = User.objects.create_user(username="tester", password="pass")
        perm = Permission.objects.get(codename="view_actor")
        user.user_permissions.add(perm)
        self.client.login(username="tester", password="pass")
        resp = self.client.get(self.url_detail)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "actors/detail.html")
        self.assertContains(resp, "Matthew Perry")
