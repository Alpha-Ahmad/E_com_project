from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name ="home"),
    path('genres', views.genres, name ="genres"),
    path('genres/<str:genre>',views.genresview, name ="genresview"),
    path('genres/<str:genre_name>/<int:prod_id>/', views.productview, name="productview")
,

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)