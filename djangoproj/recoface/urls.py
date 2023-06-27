from django.urls import path
from . import views 


urlpatterns = [
    path('',views.indexfunction),
    path('recoface/',views.recofacefunction,name="recoface"),
    path('registface/', views.registfacefunction,name="registface"),#<--追加
    path('video_feed', views.video_feed_view(), name="video_feed"),
    path('translation/', views.translatefunction,name="translation"),
    path("translation/ajax/", views.test_ajax_response,name="ajax"),

    path("registface/regist_face/", views.regist_face,name="regist_face")
]