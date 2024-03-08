from django.http import HttpResponse
from django.shortcuts import render

from .forms import CandidateForm
from .models import Exam
from django.contrib.auth.models import User

# Create your views here.
def add_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            stage = form.cleaned_data['stage']
            career = form.cleaned_data['career']

            # crear usuario
            user = User.objects.create_user(username, email, password)
            # editar usuario
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            # crear exam
            exam = Exam.objects.create(user=user, stage=stage, career=career)
            # editar exam
            exam.set_modules()
            exam.set_questions()

            html= """

            <h1>Usuario y examen creado</h1>
            <a href="/exam/add/">Agregar otro</a>
                    """
            return HttpResponse(html)
        


    form = CandidateForm()
    return render(request, 'exam/add_candidate.html', {"form": form})