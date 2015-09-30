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
    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(PhoneEmail.objects.count(), 0) 

    
class PhoneEmailModelTest(TestCase):


    def test_saving_and_retrieving_items(self):
        third_item =PhoneEmail()
        third_item.text = 'The third phoneemail'
        third_item.save()

        second_item = PhoneEmail()
        second_item.text = 'The second phoneemail'
        second_item.save()

        saved_items = PhoneEmail.objects.all()
        self.assertEqual(saved_items.count(), 2)

        third_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(third_saved_item.text, 'The third phoneemail')
        self.assertEqual(second_saved_item.text, 'The second phoneemail')

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['phoneemail_text'] = '1234567howdy@gmail.com'

        response = home_page(request)

        self.assertEqual(PhoneEmail.objects.count(), 1)  
        new_item = PhoneEmail.objects.first()  
        self.assertEqual(new_item.text, '1234567howdy@gmail.com')  

        #self.assertIn('1234567howdy@gmail.com', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':  '1234567howdy@gmail.com'}
        )
        self.assertEqual(response.content.decode(), expected_html)
