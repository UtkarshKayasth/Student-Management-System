from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')

        Student.objects.create(name=name, email=email, age=age, course=course)
        return redirect('student_list')

    return render(request, 'register.html')


def student_list(request):
    students = Student.objects.filter(is_deleted=False)
    return render(request, 'student_list.html', {'students': students})

def update_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')

    
    return render(request, 'update_student.html', {'student': student})

    
    

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.is_deleted = True  # soft delete
    student.save()
    return redirect('student_list')

def about(request):
    return render(request, 'about.html')

    

