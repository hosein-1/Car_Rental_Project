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


