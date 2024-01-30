from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .forms import LoginForm

urlpatterns=[
    path('',views.index,name='home'),
    path('contact/',views.contact ,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name='core/login.html'),name='login'),
   path('logout/',views.logoutPage, name='logout')
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)