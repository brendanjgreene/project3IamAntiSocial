from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Magazine


class MagazinePageTest(TestCase):
    def test_check_content_is_correct(self):
        magazine_page = self.client.get('/magazines/')
        self.assertTemplateUsed(magazine_page, "magazines/magazines.html")
        magazine_page_template_output = render_to_response("magazines/magazines.html",
                                                           {'magazines': Magazine.objects.all()}).content
        self.assertEqual(magazine_page.content, magazine_page_template_output)
