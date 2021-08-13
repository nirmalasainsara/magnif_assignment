from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .models import Student
from .forms import LoginForm, StudentForm, SignUpForm
from django.contrib.auth.models import User



# create project
def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("assignment:home"))

    else:
        form = StudentForm()
    context = {"form": form}
    return render(request, "assignment/student.html", context)



def home_view(request):
    student = Student.objects.all()
    context = {"student": student}
    return render(request, "assignment/home.html", context)


def student_detail_view(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {"student": student}
    return render(request, "assignment/student_detail.html", context)



def delete_student_data(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect(reverse("assignment:home"))


def update_student_data(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect(reverse("assignment:home"))
    return render(request, "assignment/student.html", {"student": student, "form": form})


def signup_view(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect(reverse("assignment:home"))

    context = {"form": form}
    return render(request, "assignment/student.html", context)


# user login page
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse("assignment:home"))
    return render(request, "assignment/student.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("assignment:home"))