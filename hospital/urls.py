from django.urls import path
from . import views
#from predict.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
#from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

app_name='predict'
urlpatterns = [
    path('', views.doc, name='doctor'),
    path('authent/', views.authenticate, name='doctor'),
    path('createpatient/', views.addPatient, name='patient'),
    path('patients/', views.allPatients, name='allpatients'),
    path('patient/delete/', views.deletePatient, name='delpatients'),
    path('patient/edit/', views.editPatient, name='editpatients'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)