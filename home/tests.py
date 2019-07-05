from django.test import TestCase
from . import views

# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/home1/')
        self.assertEquals(response.status_code,404)

    def test_home_page_contains_correct_html(self):
        response=self.client.get('/home1/')
        self.assertContains(response,'HomePage')

    def test_home_page_does_not_contain_incorrect_html(self):
        response=self.client.get('/home1/')
        self.assertNotContains(response,'Hi there! I should not be on this page')
    
    def test_view_uses_correct_templates(self):
        response=self.client.get('/home1/')
        self.assertTemplateUsed(response,'testpge.html')