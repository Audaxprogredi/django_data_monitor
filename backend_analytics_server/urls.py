# backend_analytics_server/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), # Conecta la app dashboard a la raíz
    # Ruta login/ para la vista LoginView para inicio de sesión, uso de plantilla y alias
    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),

    # Ruta logout/ para la vista LogoutView para fin de sesión, redirección y alias
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

]