from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students
# Create your views here.
def students_list(request):
    students_list = {'students_list':Students.objects.all()}
    return render(request, "crudapp/student_list.html",students_list)

def students_form(request,id=0):


    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Students.objects.get(pk=id) #model
            form = StudentForm(instance=student)
        return render(request, "crudapp/student_form.html",{'form':form})
    else:
        if id == 0:

            form = StudentForm(request.POST)
        else:
            student = Students.objects.get(pk=id)
            form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/students/list')
def students_delete(request,id):
    student = Students.objects.get(pk=id)
    student.delete()
    return redirect('/students/list')
