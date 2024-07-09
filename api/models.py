from django.db import models

# Create your models here.
class api_types:
    types = (
        ('get', 'GET'), 
        ('post', 'POST'), 
        ('patch', 'PATCH'), 
        ('put', 'PUT'), 
        ('delete', 'DELETE')
    )

class api_call(models.Model):
    api_type = models.TextField(choices=api_types.types, default='get', max_length=6)
    name = models.TextField(verbose_name='Name', blank=False, null=False, default='GET Api Call')
    endpoint = models.TextField(verbose_name='API Endpoint', blank=True, null=False)
    headers = models.TextField(verbose_name='Headers', blank=True, null=True)
    body = models.TextField(verbose_name='Body', blank=True, null=True)

