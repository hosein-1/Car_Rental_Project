from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Questions, Page
from .forms import QuestionForm


def page(request, slug):
    page_object = get_object_or_404(Page.objects.filter(is_active=True), slug=slug)

    context = {
        'page': page_object,
    }
    return render(request, 'pages/page.html', context)


def questions_list(request):
    questions = Questions.objects.filter(parent=None)

    context = {
        'questions': questions,
        'banner': False,
    }
    return render(request, 'pages/questions_list.html', context)


def ask_question(request):

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
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'question_id': form,
        'banner': False,
    }
    return render(request, 'pages/ask_questions.html', context)


def question(request, id):
    question_obj = get_object_or_404(Questions.objects.filter(parent=None), id=id)

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
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'question': question_obj,
        'banner': False,
    }
    return render(request, 'pages/question.html', context)


