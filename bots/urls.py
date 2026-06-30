from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotViewSet, ScenarioViewSet, StepViewSet, chat_view


router = DefaultRouter()
router.register(r'bots', BotViewSet)
router.register(r'scenarios', ScenarioViewSet)
router.register(r'steps', StepViewSet)

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('', include(router.urls)),
]