from django.urls import path
from .views import chatbot_response, chat_history,welcome_view,delete_chat_history


urlpatterns = [
    path("welcome/", welcome_view, name="welcome"),
    path("chatbot-response/", chatbot_response, name="chatbot_response"),
    path("history/", chat_history, name="chat_history"),
    path("delete-history/", delete_chat_history, name="delete_chat_history"),
]
