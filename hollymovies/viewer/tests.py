import time
from platform import release
from telnetlib import EC

from django.template.defaultfilters import title
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from .models import Genre, Actor, Director, Movie
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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


class MovieViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.genre = Genre.objects.create(name="Horror", description="Strašidelné filmy")
        self.director = Director.objects.create(name="Quentin", surname="Tarantino", birth_day="1963-03-27")
        self.movie = Movie.objects.create(
            title="Pulp Fiction: Historky z podsvětí",
            genre=self.genre,
            rating=10,
            released=1994,
            description="Nejkultovnější z kultovních filmů 90. let je autorskou Biblí Quentina Tarantina, který v tomto opusu definoval základní prvky své režisérské poetiky a vytvořil dílo rozněcující náročné kritiky na festivalu v Cannes, levicové a pravicové intelektuály i zedníky dopřávající si po těžké šichtě trochu oddychu. Pulp Fiction je multižánrovým opusem, který přetéká fetišistickými detaily a popkulturními odkazy a zároveň dokonale funguje jako svrchovaně napínavý film rozvržený do inovativní příběhové struktury. Chcete vidět homosexuální znásilnění sbližující dva nepřátele na život a na smrt?",
            director=self.director
        )
        self.url_list = reverse("movies")
        self.url_detail = reverse("movie_detail", args=[self.movie.pk])

    def test_actor_list(self):
        resp = self.client.get(self.url_list)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "movies/index.html")
        self.assertIn(self.movie, resp.context["object_list"])

"""


class SeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_argument("--start-maximized")

        cls.selenium = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    """
    def test_homepage_title(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.assertIn("Movies", self.selenium.title)
    """

    def test_language_dropdown_with_selenium(self):
        self.selenium.get(f"{self.live_server_url}/")
        time.sleep(10)
        dropdown_btn = self.selenium.find_element(By.ID, "langDropdown3")
        dropdown_btn.click()
        time.sleep(10)

        wait = WebDriverWait(self.selenium, 10)
        select_elem = wait.until(
            EC.visibility_of_element_located((By.NAME, "language"))
        )

        time.sleep(10)
        select = Select(select_elem)
        select.select_by_value("en")

        time.sleep(5)
        wait.until(
            EC.staleness_of(select_elem)
        )
        new_select = self.selenium.find_element(By.NAME, "language")
        new_selected = new_select.find_element(By.CSS_SELECTOR, "option:checked")
        self.assertEqual(new_selected.get_attribute("value"), "en")