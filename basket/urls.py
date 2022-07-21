from django.urls import path
import basket.views as bv

urlpatterns = [
    path('', bv.Index.as_view(), name='basket_index'),
    path('set/', bv.Set.as_view(), name='basket_set'),
    path('del/', bv.Delete.as_view(), name='basket_del'),
]