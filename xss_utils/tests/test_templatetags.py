"""
Tests for templates tags.
"""

from django.template import Context, Template
from django.test import TestCase


class HtmlEscapeTemplateTagTest(TestCase):
    def test_xss_escape_rendered(self):
        """ Verify htmlescape filter escapes javascript injection """
        context = Context({})
        template_to_render = Template(
            '{% load html %}'
            '{{ "<script>alert(\'xss\')</script>" | htmlescape}}'
        )
        rendered_template = template_to_render.render(context)
        self.assertEqual(rendered_template.find('<script>'), -1)