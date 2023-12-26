from django.urls import path
from . import views
urlpatterns=[
    path('studenthome/',views.studenthome,name='studenthome'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('response/',views.response,name='response'),
    path('changepass/',views.changepass,name='changepass'),
    path('viewstudentbook/',views.viewstudentbook,name='viewstudentbook'),
]