from django.urls import path

from . import views
app_name = 'polos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:pk>/resualts/', views.ResualtsView.as_view(), name='resualts'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
