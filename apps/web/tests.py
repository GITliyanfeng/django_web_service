from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpResponse, HttpRequest
from web.views import index, view_post
from web.models import BlogPost


# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_returns_currect_html(self):
        request = HttpRequest()
        response = index(request)
        # 测试主页的标题是否是正确的
        self.assertIn(b'<title>Welcome to my blog</title>', response.content)

    def test_home_page_is_has_content(self):
        from datetime import datetime
        data = {
            'title': 'this is a test',
            'markdown': 'this is a blog',
            'slug': 'this-is-a-test-leee',
            'author': 'leee',
            'add_time': datetime.now
        }
        BlogPost.objects.create(**data)
        response = self.client.get('/')
        self.assertIn(b'this is a blog', response.content)


class BlogpostTest(TestCase):
    # 测试这种路由模式是否能调用view_post视图函数
    def test_web_url_resolves_to_blog_post_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, view_post)

    # 测试创建数据
    def test_web_create_with_view(self):
        from datetime import datetime
        data = {
            'title': 'this is a test',
            'markdown': 'this is a blog',
            'slug': 'this-is-a-test-leee',
            'author': 'leee',
            'add_time': datetime.now
        }
        BlogPost.objects.create(**data)
        response = self.client.get('/blog/this-is-a-test-leee.html')
        self.assertIn(b'this is a blog', response.content)


# 自动化的测试
from django.test import LiveServerTestCase
from selenium import webdriver


class HomePageLiveTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_visit_homepage(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url, '/')
        )
        self.assertIn("Welcome to my blog", self.selenium.title)


class BlogpostDetailLiveTest(LiveServerTestCase):
    def setUp(self):
        from datetime import datetime
        data = {
            'title': 'this is a test',
            'markdown': 'this is a blog',
            'slug': 'this-is-a-test-leee',
            'author': 'leee',
            'add_time': datetime.now
        }
        BlogPost.objects.create(**data)
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super(BlogpostDetailLiveTest, self).tearDown()

    def test_visit_blog_post(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url, "/blog/this-is-a-test-leee.html")
        )
        self.assertIn("this is a test", self.selenium.title)


class TestHomePageContent(LiveServerTestCase):
    def setUp(self):
        from datetime import datetime
        data = {
            'title': 'this is a test',
            'markdown': 'this is a blog',
            'slug': 'this-is-a-test-leee',
            'author': 'leee',
            'add_time': datetime.now
        }
        BlogPost.objects.create(**data)
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_visit_blog_post(self):
        self.selenium.get(
            "%s%s" % (self.live_server_url, "/")
        )
        # 获取页面的元素
        self.selenium.find_element_by_link_text("this is a test").click()
        self.assertIn('this is a test', self.selenium.title)
