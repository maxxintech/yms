from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign_up, name='user_sign'),
    path('dashboard', views.user_dashboard, name='user_dashboard'),
    path('login', views.sign_in, name='login_user'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update',views.profile_update,name='profile-update'),
    path('profile/', views.profile, name='profile-display'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)