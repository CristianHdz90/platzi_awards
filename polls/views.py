import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    context = {
        "latest_question_list": Question.objects.all()
    }
    return render(
        request=request,
        template_name="polls/index.html",
        context=context
    )


def detail(request, question_id):
    '''This will show all the information about the question'''
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request=request,
        template_name="polls/detail.html",
        context={"question": question}
    )


def results(request, question_id):
    '''Show the number of votes of one question'''
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request=request,
        template_name="polls/results.html",
        context={
            "question": question
        }
    )


def vote(request, question_id):
    '''This will show all the information about the question'''
    question = get_object_or_404(Question, pk=question_id)

    try:
        choice_id = request.POST["choice"]
        selected_choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(
            request=request,
            template_name="polls/detail.html",
            context={
                "question": question,
                "error_message": "No choice selected"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            redirect_to=reverse(viewname="polls:results", args=(question.id,))
        )