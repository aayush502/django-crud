from django.shortcuts import render, redirect
from django.views import View
from .models import Student
import pdb
class CreateStudent(View):
    def get(self, request):
        return render(request, "crud/create.html", context={})

    def post(self, request):
        name = request.POST['name']
        grade = request.POST['grade']
        roll = request.POST['roll']
        phone = request.POST['phone']
        try:
            if request.POST['male']=='on':
                Student.objects.create(name=name, grade = grade, roll_no = roll, phone = phone, gender = "male")    
        except:
            Student.objects.create(name=name, grade = grade, roll_no = roll, phone = phone, gender = "female")
        return redirect('create')

class ViewStudent(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, "crud/studentview.html", context={"data":student})

class EditStudent(View):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        return render(request, "crud/edit.html", context={"data":student})

    def post(self, request, id):
        student = Student.objects.filter(id=id).first()
        student.name = request.POST['name']
        student.grade = request.POST['grade']
        student.roll = request.POST['roll']
        student.phone = request.POST['phone']
        try:
            if 'on' not in request.POST['male']:
                student.gender = "female"
                student.save()
        except:
            student.gender = "male"
            student.save()
        return redirect('home')
   
class DeleteStudent(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        return render(request, "crud/delete.html", context={"data":student})

    def post(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect("home")