from django.urls import register_converter, path
import basket.views as bv
import basket.custom_converters as bcc

register_converter(bcc.NegativeIntConverter, 'negint')

urlpatterns = [
    path(
        '',
        bv.index.as_view(),
        name='basket_index'
    ),
    path(
        'modify/<int:id>/<negint:quantity>',
        bv.modify_class.as_view(),
        name='basket_modify'
    ),
    path(
        'modify/<int:id>/<negint:quantity>/<str:redirect_url>',
        bv.modify_class.as_view(),
        name='basket_modify'
    ),
    path(
        'remove/<int:id>',
        bv.remove.as_view(),
        name='basket_remove'
    ),
    path(
        'clear',
        bv.clear_view.as_view(),
        name='basket_clear'
    ),
]
