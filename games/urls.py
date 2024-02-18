from django.urls import path
from games.views import Lists, Info

urlpatterns = [
    path('', Lists.as_view(), name = 'home'),
    path('<slug:slug>/', Info.as_view(), name = 'game')
]
