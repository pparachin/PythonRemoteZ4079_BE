from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from .models import Genre, Actor, Director, Movie

class ModelsTest(TestCase):
    "Vytvoření instancí tříd modelů"
    def setUp(self):
        self.genre = Genre.objects.create(name="Horror", description="Strašidelné filmy")
        self.actor = Actor.objects.create(name="Will", surname="Smith", birth_day="1976-3-2")
        self.director = Director.objects.create(name="Quentin", surname="Tarantino", birth_day="1963-03-27")


    def test_genre(self):
        self.assertEqual(str(self.genre), "Horror")

    def test_actor_str(self):
        self.assertEqual(str(self.actor), "Will Smith")

    def test_director_str(self):
        self.assertEqual(str(self.director), "Quentin Tarantino")


    "Úkol: vytvořit to stejné pro film"
    "Přidat k filmu herce"

"""
class ActorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.actor = Actor.objects.create(
            name="Matthew", surname="Perry", birth_day="1969-08-19"
        )
        self.url_list = reverse("actors")
        self.url_detail = reverse("actor_detail", args=[self.actor.pk])

    def test_actor_list(self):
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "actors/index.html")
        self.assertIn(self.actor, resp.context["object_list"])

    def test_actor_detail_permission_denied(self):
        resp = self.client.get(self.url_detail)
        self.assertNotEqual(resp.status_code, 200)
        self.assertIn(resp.status_code, (302, 403))

    def test_actor_detail_with_permission(self):
        
        user = User.objects.create_user(username="tester", password="pass")
        perm = Permission.objects.get(codename="view_actor")
        user.user_permissions.add(perm)
        self.client.login(username="tester", password="pass")
        resp = self.client.get(self.url_detail)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "actors/detail.html")
        self.assertContains(resp, "Alice Wonder")
       
"""