from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from signup.views import home_page 
from signup.models import PhoneEmail


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertTrue(response.content.startswith(b'<html>'))  
        #self.assertIn(b'<title>Sign Up Form</title>', response.content)  
        #self.assertTrue(response.content.strip().endswith(b'</html>')) 


class PhoneEmailModelTest(TestCase):


    def test_saving_and_retrieving_items(self):
        first_item =PhoneEmail()
        first_item.text = 'The first phoneemail is'
        first_item.save()

        second_item = PhoneEmail()
        second_item.text = 'The second phoneemail is'
        second_item.save()

        saved_items = PhoneEmail.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first phone email')
        self.assertEqual(second_saved_item.text, 'The second phoneemail is')


