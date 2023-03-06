from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import LoginForm, SignUpForm_Student, SignUpForm_teacher
from django.contrib.auth.decorators import login_required
from .models import RegisterTeacher, RegisterStudent, Details
from django.contrib import messages
from .forms import AadhaarForm, DetailForm, TimeSheetForm, GiveTaskForm, SubmitResultForm
from .models import Aadhaar, TimeSheet, TaskModel, SubmitResult
from django.http import JsonResponse
from authentication.Calculation import calculate_mathematical_operations
from word2number import w2n


#  icons-argon - https://demos.creative-tim.com/black-dashboard/examples/icons.html

def login_view(request):  # login view
    form = LoginForm(request.POST or None)  # login form

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")  # get the data
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # login the user if user have credentials
                messages.success(request, "User Logged in Successfully")
                return redirect("home")  # back to home with credentials
            else:
                messages.error(request, "Invalid Credentials")
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
            messages.error(request, "Invalid Credentials, Returned to login page.")

    return render(request, "accounts/login.html", {"form": form, "msg": msg})  # rendering the login template


def register_student(request):
    msg = None
    success = False

    if request.method == "POST":  # checking the method is POST or not
        form = SignUpForm_Student(request.POST)
        if form.is_valid():  # checking the form is valid or not
            form.save()
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            raw_password = form.cleaned_data.get("password1")
            standard = form.cleaned_data.get('standard')
            section = form.cleaned_data.get('section')
            stream = form.cleaned_data.get('stream')  # grabing the data from the form
            roll_no = form.cleaned_data.get('roll_no')
            student_id = form.cleaned_data.get('student_id')
            email = form.cleaned_data.get('email')
            student = RegisterStudent.objects.create_account(username=username, first_name=first_name,
                                                             last_name=last_name,
                                                             password=raw_password)  # creating a student object from the RegisterStudent model to store the credentials
            student.standard = standard
            student.section = section
            student.stream = stream
            student.roll_no = roll_no
            student.student_id = student_id
            student.email = email  # store the extra attributes
            student.save()  # save
            messages.success(request, "Student registered successfully. Login with credentials.")
            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            messages.error(request, "Invalid Credentials. Register again with correct credentials.")
            msg = 'Form is not valid'
    else:
        form = SignUpForm_Student()

    return render(request, "accounts/register_student.html", {"form": form, "msg": msg, "success": success})


def register_teacher(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm_teacher(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            raw_password = form.cleaned_data.get("password1")
            subject = form.cleaned_data.get("subject")
            classes_taught = form.cleaned_data.get("classes_taught")
            contact_number = form.cleaned_data.get("contact_number")  # getting the data from the form
            teacher_id = form.cleaned_data.get("teacher_id")
            email = form.cleaned_data.get("email")
            teacher = RegisterTeacher.objects.create_account(username=username, first_name=first_name,
                                                             last_name=last_name,
                                                             password=raw_password)  # creating a teacher object from RegisterTeacher class to store the data
            teacher.subject = subject
            teacher.classes_taught = classes_taught
            teacher.contact_number = contact_number
            teacher.teacher_id = teacher_id
            teacher.email = email  # store the extra attributes
            teacher.save()
            messages.success(request, "Teacher registered successfully. Login with credentials.")
            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            messages.error(request, "Invalid Credentials. Register again with correct credentials.")
            msg = 'Form is not valid'
    else:
        form = SignUpForm_teacher()

    return render(request, "accounts/register_teacher.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url='/login/')
def profile(request):
    student_object = RegisterStudent.objects.filter(username=request.user).first()
    teacher_object = RegisterTeacher.objects.filter(username=request.user).first()
    print(student_object)
    if student_object:
        data = dict(
            username=request.user,
            first_name=student_object.first_name,
            last_name=student_object.last_name,
            standard=student_object.standard,
            section=student_object.section,
            stream=student_object.stream,
            roll_no=student_object.roll_no,
            student_id=student_object.student_id,
            email=student_object.email
        )
        return render(request, 'accounts/profile_student.html', data)
    elif teacher_object:
        data = dict(
            username=request.user,
            first_name=teacher_object.first_name,
            last_name=teacher_object.last_name,
            subject=teacher_object.subject,
            classes_taught=teacher_object.classes_taught,
            contact_number=teacher_object.contact_number,
            teacher_id=teacher_object.teacher_id,
            email=teacher_object.email
        )
        return render(request, 'accounts/profile_teacher.html', data)
    else:
        return redirect('login')


@login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html')  # home page


@login_required(login_url="login")
def logout(request):
    auth_logout(request)  # logout
    messages.success(request, "user logged out successfully.")
    return redirect('login')


@login_required(login_url='/login/')
def give_tasks(request):
    teacher = request.user.username
    teacher_object = RegisterTeacher.objects.filter(username=request.user).first()
    if teacher_object:
        if request.user.is_authenticated:
            form = GiveTaskForm()
            if request.method == 'POST':
                form = GiveTaskForm(request.POST)
                if form.is_valid():
                    task_data = form.cleaned_data['task']
                    task = TaskModel(task=task_data, teacher=teacher)
                    task.save()
                    messages.success(request, "You have added a new task.")
                    return redirect('home')
            else:
                form = GiveTaskForm()
        return render(request, 'accounts/task.html', {'form': form})
    else:
        messages.error(request, "You are not a valid teacher. Please login with teacher id and password.")
        return redirect('login')


@login_required(login_url='/login/')
def show_task(request):
    if request.user.is_authenticated:
        tasks = TaskModel.objects.all()
        all_tasks = []
        all_teachers = []
        task_id = []
        for i in tasks:
            all_tasks.append(i.task)
            all_teachers.append(i.teacher)
            task_id.append(i.id)
        data = list(zip(all_tasks, all_teachers, task_id))
        return render(request, 'accounts/show_details.html', {'data': data})


@login_required(login_url='/login/')
def submit_result(request, pk):
    student = RegisterStudent.objects.filter(username=request.user).first()
    if student:
        task_object = get_object_or_404(TaskModel, pk=pk)
        student = request.user
        task = task_object.task
        check_if_student_already_exists = SubmitResult.objects.filter(student=request.user, task=task).first()
        if check_if_student_already_exists:
            messages.success(request, "You have already attended this question. Please answer another question.")
            return redirect('home')
        if request.user.is_authenticated:
            form = SubmitResultForm()
            if request.method == 'POST':
                form = SubmitResultForm(request.POST)
                if form.is_valid():
                    answer = form.cleaned_data['answer']
                    result = SubmitResult(task=task, student=student, answer=answer)
                    result.save()
                    messages.success(request, "You have successfully submitted the answer.")
                    return redirect('home')
            else:
                form = SubmitResultForm()
        return render(request, 'accounts/submit_result.html', {'form': form, 'task': task})
    else:
        messages.error(request, "You are not a valid student. Please login with student id and password.")
        return redirect('login')


@login_required(login_url='/login/')
def check_answers_and_show_results(request):
    results = SubmitResult.objects.all()
    students = []
    answers = []
    tasks = []
    correct_answers = []
    is_correct = []
    for i in results:
        students.append(i.student)
        answers.append(i.answer)
        tasks.append(i.task)
        correct_answer = calculate_mathematical_operations(i.task)
        correct_answers.append(correct_answer)
        if type(int(i.answer)):
            if int(i.answer) == correct_answer:
                is_correct.append(True)
            else:
                is_correct.append(False)
        else:
            answer = w2n.word_to_num(i.answer)
            if answer == correct_answer:
                is_correct.append(True)
            else:
                is_correct.append(False)
    data = list(zip(tasks, answers, students, correct_answers, is_correct))
    return render(request, 'accounts/check_and_show_details.html', {'data': data})

