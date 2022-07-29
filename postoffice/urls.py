from django.urls import path
import postoffice.views as pov

urlpatterns = [
    path('newsletter/', pov.write_newsletter.as_view(), name='write_newsletter'),
]
