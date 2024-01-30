from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Questions
from .forms import QuestionForm


@login_required()
def ask_question(request):
    questions = Questions.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_object = form.save(commit=False)
            question_object.author = request.user
            try:
                question_object.parent = form.cleaned_data['parent']

            except:
                question_object.parent = None
            form.save()

        return render(request, 'pages/questions.html', {'form': form, 'questions': questions})

    else:
        form = QuestionForm()
        return render(request, 'pages/questions.html', {'form': form, 'questions': questions})


def about_us_view(request):
    return render(request, 'pages/about_us.html')