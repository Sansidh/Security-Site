from django.conf.urls import include, url

urlpatterns = [
    url(r'^hello/', 'encrypt.views.hello', name = 'hello'),
]