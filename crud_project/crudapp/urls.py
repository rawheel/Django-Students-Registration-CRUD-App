
from django.urls import path,include
from . import  views
urlpatterns = [
    path('',views.students_form,name="student_insert"),
    path('<int:id>/',views.students_form,name="student_update"),
    path('delete/<int:id>/',views.students_delete,name="student_delete"),
    path('list/',views.students_list,name="student_list")
]