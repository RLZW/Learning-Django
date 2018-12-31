"""platzigram urls"""


from django.urls import path

from platzigram import views as local_views
from posts import views as post_views


urlpatterns = [

    path('hello-world/', local_views.hello_word),
    path('sort/', local_views.sort),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', post_views.list_posts),
]
