from django.conf.urls import url
from django.urls import path
from .views import *
urlpatterns = [
    url(r'^create/$', CreateStudent.as_view(), name="create"),
    url(r'^$', ViewStudent.as_view(), name='home'),
    # path('edit/<int:id>', edit_student, name='edit'),
    path('delete/<int:id>', DeleteStudent.as_view(), name="delete"),
    url(r'^edit/(?P<id>\d+)/$', EditStudent.as_view(), name='edit'),
]