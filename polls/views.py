import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    response = "Main page of Platzi awards"
    return HttpResponse(
        content=json.dumps({"message": response})
    )


def detail(request, question_id):
    '''This will show all the information about the question'''
    response = f"You're seeing the question No: {question_id}"
    return HttpResponse(
        content=json.dumps({"message": response})
    )


def results(request, question_id):
    '''Show the number of votes of one question'''
    response = f"You're seeing the results of the question No: {question_id}"
    return HttpResponse(
        content=json.dumps({"message": response})
    )


def vote(request, question_id):
    '''This will show all the information about the question'''
    response = f"You're voting to the question No: {question_id}"
    return HttpResponse(
        content=json.dumps({"message": response})
    )