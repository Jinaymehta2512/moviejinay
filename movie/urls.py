from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('movie/<int:movie_id>',views.detail, name='detail'),
    path('movie/<int:movie_id>/create',views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete', views.deletereview,name='deletereview'),
]