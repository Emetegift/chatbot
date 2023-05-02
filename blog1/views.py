from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot_corpus import chatbot




# bot = ChatBot('chatbot', read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

# #Training chatbot to respond to users questions.
# #  The first element in the list_to_train should be the possible users question and, the second should be the chatbot response 
# list_to_train = [
#     "hi",
#     "hi, there",
#     "what is your name?",
#     "I am your companion",
#     "what makes you special?",
#     "Solving poeple's problems makes me special"
# ]
# # # nlp = spacy.load("en_core_web_sm")
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train) 

def index(request):
     return render(request,'blog1/index.html')


def specific(request):
   return HttpResponse('specific')

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    return HttpResponse(userMessage)