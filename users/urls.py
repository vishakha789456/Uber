from django.urls import path,includefrom  
from  .views import *


from users.urls import *
urlpatterns=[
    path('get-all-students',GetstudentsViews.as_view())
]