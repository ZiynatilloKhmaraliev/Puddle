from django.urls import path
from . import views

app_name='inbox'
urlpatterns=[
    path('new/<item_pk>/',views.new_conversation,name='new'),
    path('inbox/',views.inbox,name='inbox'),
    path('<int:pk>/',views.detail,name='detail')
]