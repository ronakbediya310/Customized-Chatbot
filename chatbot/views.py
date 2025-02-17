from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from .models import ChatHistory
from .model import ChatbotModel

## Welcome view available after sucessfull login 
@login_required
def welcome_view(request):
    """Redirects to chatbot home after successful login."""
    return render(request, "chatbot/welcome.html")

## Chat response view 
@login_required
def chatbot_response(request):
    chatbot = ChatbotModel(user=request.user)

    if (
        request.method == "POST"
        and request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):
        question = request.POST.get("question", "").strip()
        operation = request.POST.get("operation", "").strip()
        raw_que = question
        ## modifying question if any quick action button has been pressed;
        if operation and question:
            if operation == "explain":
                question = f"Explain this code in simple terms:\n{question}"
            elif operation == "debug":
                question = f"Find and fix errors in this code:\n{question}"
            elif operation == "optimize":
                question = f"Optimize this code for better performance:\n{question}"
            elif operation == "convert":
                question = f"Convert this code into a different language:\n{question}"
            elif operation == "generate":
                question = f"Generate a code snippet for:\n{question}"
        ## feeding question to LLM;
        if question:
            bot_response = chatbot.ask_chatbot(question)
        else:
            return JsonResponse({"error": "Please enter a question first."}, status=400)

        # Save the chat in the database
        chat_entry = ChatHistory.objects.create(
            user=request.user,
            question=raw_que,
            response=bot_response["bot_response"],
            timestamp=bot_response["timestamp"],
        )

        # Save chat history in session
        if "current_chat" not in request.session:
            request.session["current_chat"] = []

        new_chat = {
            "user": raw_que,
            "bot": bot_response["bot_response"],
            "timestamp": bot_response["timestamp"],
        }

        request.session["current_chat"].append(new_chat)
        request.session.modified = True
        return JsonResponse(new_chat)
    ## GET req rendering;
    return render(
        request,
        "chatbot/chat.html",
        {"chat_history": request.session.get("current_chat", [])},
    )

## view chat history page
@login_required
def chat_history(request):
    """Fetches and displays chat history in history.html."""
    chat_data = ChatHistory.objects.filter(user=request.user).order_by("-timestamp")
    return render(request, "chatbot/history.html", {"chat_data": chat_data})

## delete chat history
@login_required
def delete_chat_history(request):
    """Deletes all chat history for the logged-in user."""
    if request.method == "POST":
        ChatHistory.objects.filter(user=request.user).delete()
        request.session["current_chat"] = []
    return redirect("chatbot_response")
