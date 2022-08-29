from django.urls import path
import postoffice.views as pov

urlpatterns = [
    path(
        'newsletter/',
        pov.write_newsletter.as_view(),
        name='write_newsletter'
    ),
    path('signup/', pov.signup_newsletter.as_view(), name='signup_newsletter'),
    path(
        'cancel_newsletter/<int:id>',
        pov.cancel_newsletter.as_view(),
        name='cancel_newsletter'
    ),
]
