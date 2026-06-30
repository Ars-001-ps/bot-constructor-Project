from django.shortcuts import render
from rest_framework import viewsets
from .models import Bot, Scenario, Step
from .serializers import BotSerializer, ScenarioSerializer, StepSerializer
from django.http import JsonResponse
from bots.chat_bot.conditions import response

class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer



def chat_view(request):
    bot_response = None
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        bot_response = response(user_message)
    return render(request, 'bots/chat.html', {'bot_response': bot_response})