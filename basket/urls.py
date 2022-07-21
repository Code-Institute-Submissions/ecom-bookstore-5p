from django.urls import register_converter, path
import basket.views as bv
import basket.custom_converters as bcc

register_converter(bcc.NegativeIntConverter, 'negint')

urlpatterns = [
    path(
        '',
        bv.Index.as_view(),
        name='basket_index'
    ),
    path(
        'modify/<int:id>/<negint:quantity>',
        bv.Modify.as_view(),
        name='basket_modify'
    ),
    path(
        'remove/',
        bv.Remove.as_view(),
        name='basket_remove'
    ),
]