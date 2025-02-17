import os
import json
from datetime import datetime
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from chatbot.prompt import CUSTOM_PROMPT
from .models import ChatHistory
import re


class ChatbotModel:
    """Chatbot Model using LangChain with Groq API & Django DB"""

    # Model initialization code
    def __init__(self, user=None):
        self.user = user
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in environment variables.")

        self.llm = ChatGroq(
            api_key=api_key, model="llama-3.3-70b-versatile", temperature=0
        )
        self.prompt = PromptTemplate(
            template=CUSTOM_PROMPT, input_variables=["history", "question"]
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    ## Code for asking the question and getting response
    def ask_chatbot(self, question):
        """Handles user queries and uses DB history."""
        history = ChatHistory.objects.filter(user=self.user).order_by("-timestamp")[:5]

        # Format history for AI
        history_text = "\n".join(
            [f"You: {chat.question}\nAI: {chat.response}" for chat in history]
        )

        response = self.chain.run({"history": history_text, "question": question})
        response = self.format_response(response)
        return {
            "user_message": question,
            "bot_response": response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    ## Code for formatting the response given by LLM model;
    def format_response(self, response):
        """Formats the bot's response for better readability."""
        # Convert markdown-like formatting to HTML-friendly format
        response = re.sub(r"\*\*(.*?)\*\*", r"", response)
        response = re.sub(r"\*(.*?)\*", r"", response)

        return response
