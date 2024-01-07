from django.urls import path
from . import views
urlpatterns = [
   path('',views.home, name="home"),
   path('login/',views.login_user, name="login"),
   path('logout/',views.logout_user, name="logout"),
   path('about/',views.about, name='about'),
   path('register/',views.register_user, name='register'),
   path('product/<int:pk>',views.product_view, name='product_view'),
   path('category/<str:foo>',views.category_view, name='category'),
]
