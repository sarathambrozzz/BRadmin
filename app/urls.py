
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^BRadmin_index$', views.BRadmin_index, name='BRadmin_index'),
    re_path(r'^$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
    re_path(r'^BRadmin_Training$', views.BRadmin_Training,name='BRadmin_Training'),
    re_path(r'^BRadmin_trainingteam1$', views.BRadmin_trainingteam1,name='BRadmin_trainingteam1'),
    re_path(r'^BRadmin_trainerstable$', views.BRadmin_trainerstable,name='BRadmin_trainerstable'),
    re_path(r'^BRadmin_topictable$', views.BRadmin_topictable,name='BRadmin_topictable'),
    re_path(r'^BRadmin_completedtasktable$', views.BRadmin_completedtasktable,name='BRadmin_completedtasktable'),
    re_path(r'^BRadmin_trainingprofile$', views.BRadmin_trainingprofile,name='BRadmin_trainingprofile'),
    re_path(r'^BRadmin_traineestable$', views.BRadmin_traineestable,name='BRadmin_traineestable'),
    
]
