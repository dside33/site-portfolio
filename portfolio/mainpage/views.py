from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'mainpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["technologies"] = [
            {'name': 'Django', 'image': 'django.png'},
            {'name': 'PostgreSQL', 'image': 'postgresql.png'},
            {'name': 'REST API', 'image': 'rest.webp'},
            {'name': 'Postman', 'image': 'postman.svg'},
            {'name': 'Celery', 'image': 'celery.png'},
            {'name': 'Redis', 'image': 'redis.png'},
            {'name': 'Git', 'image': 'git.png'},
        ]
        return context
    
