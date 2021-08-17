
#Chatbot using NLTK Library in Python:

import nltk
from nltk.chat.util import Chat ,reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}


pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"how are you ?",
        ["I'm good & How about You ?",]
    ],
    [
        r"I am fine",
        ["Great to hear that.What should I do for you?",]
    ],
    [
        r"any issue",
        ["Not at all",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"Do you want to ask me anything?",
        ["Yes",]
    ],
    [
        r"just tell me about yourself",
        ["i am Rule based chatbot programmed using Python's NLTK library."]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) would it be ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"What do you want to ask?",
        ["are u single? XD",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"What does a chat bot means ?",
        ["A chatbot is a smart application that reduces human work and helps an organization to solve basic queries of the customer. ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Robert Downey Jr"]
    ],
    [
        r"What is NLTK?",
        ["A wonderful tool for teaching, and working in, computational linguistics using Python"]
    ],
    [
        r"quit",
        ["Thanx to chat with me. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("***********************Chatbot***************************")
    chat = Chat(pairs, reflections)
    chat.converse()

#initiate the conversation
if __name__ == "__main__":
     chat()



