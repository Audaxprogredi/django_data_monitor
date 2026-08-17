# backend_analytics_server/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de autenticación primero
    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # La app dashboard va al final para que respete las redirecciones de la raíz
    path('', include('dashboard.urls')), 
]