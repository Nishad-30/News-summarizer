from django.shortcuts import render, redirect
from Dashboard.models import *
import google.generativeai as genai
from newsdataapi import NewsDataApiClient
import random
# from scipy.spatial.distance import cosine
# import numpy as np
# from sentence_transformers import SentenceTransformer, util
# from LexRank import degree_centrality_scores

message = ["","Account already exist", "Password does not match", "Email does not exist", "Password is incorrect", "Category not found"]
a = 0
id = "demo@gmail.com"
name = "Guest User"
google_api = "AIzaSyCSLkU-RU93RQjVoajAnNqLBiLz4qLrw5s"
news_api = "pub_78522cfd3d199c17ff7f244172473128e3c27"
genai.configure(api_key=google_api)

def summarizer(records):
    # model = genai.GenerativeModel('gemini-pro')
    model = genai.GenerativeModel('gemini-1.5-flash')
    for record in records:
        try:
            promt = f'Based on the title of the news given as "{record[0]}" and the description as "{record[2]}".Provide me the summary of the news article in 150 words and in the form of paragrapgh'
            response = model.generate_content(promt)
            text = response.text
            record[2] = text
        except:
            records.remove(record)
    return records

def error(request):
    return render(request, 'error.html', {"message": message[a]})

def signup(request):
    global name
    global id
    global a 
    email = request.POST.get('email')
    name0 = request.POST.get('name')
    password = request.POST.get('password')
    repass = request.POST.get('repass')
    data =  display_table("accounts")
    if request.method == 'POST':
        if password==repass:
            for i in data:
                if email==i[0]:
                    a=1
                    return redirect('error')
            val = (email, name0, password)
            sql = "%s,%s,%s"
            name = name0
            id = email
            inserting("accounts", sql, val)
            return redirect('dashboard')
        else:
            a=2
            return redirect('error')
    return render(request, 'signup.html')


def login(request):
    global name
    global id
    global a
    email = str(request.POST.get('email'))
    password = str(request.POST.get('password'))
    data = display_table("accounts")
    if request.method == 'POST':
        for i in data:
            if i[0]==email:
                if i[2]==password:
                    name = i[1]
                    id = email
                    return redirect('dashboard')
                else:
                    a=4
                    return redirect('error')
            else:
                a=3
                return redirect('error')
    return render(request, 'login.html')



# def summmarizer(record,topic):
#     model = SentenceTransformer('stsb-roberta-large')
#     embedding1 = model.encode(topic, convert_to_tensor=True)
#     for i in record:
#         embedding2 = model.encode(i[3], convert_to_tensor=True)
#     # compute similarity scores of two embeddings
#         cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
#         similarity_scores = cosine_scores.item()
#         centrality_scores = degree_centrality_scores(similarity_scores, threshold=None)
#         response = np.argsort(-centrality_scores)
#         record[3] = response
#     return record


def news_article(topic):
    # pub_48565244df63a91c588714930796ea8473814
    # API key authorization, Initialize the client with your API key
    api = NewsDataApiClient(apikey=news_api)
    # You can pass empty or with request parameters {ex. (country = "us")}
    cat = topic.lower()
    response = api.latest_api(q="", country = "in", language="en", category=cat)
    rec = response["results"]
    record = []
    id = 100
    cnt = 0
    for i in rec:
        if i["description"] == "None" or i["description"] == None:
            continue
        data = []
        title = i["title"]
        img = i["image_url"]
        link = i["link"]
        # descr = summarizer(i["title"], i["description"], i["link"])
        descr = i['description']
        id = id+cnt
        ratio = round(random.uniform(0.3,0.4),3)
        data = [title, img, descr, link, str(id),ratio]
        record.append(data)
        cnt= cnt+1
    return summarizer(record)


def categories(request):
    article = ""
    context = {}
    
    if request.method == "POST":
        selected_category = request.POST.get("category")
        if selected_category:
            article = selected_category  # Now assign selected_category to article
    else:
        selected_category = None

    record = news_article(article)  # You pass selected category name here
    context["record"] = record
    return render(request, 'news.html', context)


# def categories(request):
#     global a 
#     article = ""
#     context = {}
#     categoriesall = ["Business", "Health", "Movies", "Sport", "Science", "Education", "Technology", "Politics", "Crypto"]
#     if request.method == "POST":
#         selected_category = request.POST.get("category")
#     print(selected_category)
#     record = news_article(article)
#     context["record"] = record
#     return render(request, 'news.html',context)
#ResourceExhausted
#ValueError

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    context = {}
    title = "Joe Biden celebrates Diwali at White House, lauds Kamala Harris: ‘I am proud that…’"
    img = "https://www.hindustantimes.com/ht-img/img/2024/10/29/550x309/US-POLITICS-RELIGION-DIWALI-BIDEN-9_1730166932980_1730166968801.jpg"
    descr = "US President Joe Biden celebrated Diwali on Monday at the White House in an event attended by more than 600 eminent Indian Americans, reported news agency PTI.Joe Biden celebrates Diwali at White House, lauds Kamala Harris: ‘I am proud that…’ByHT News DeskOct 29, 2024 08:06 AM ISTUS President Joe Biden addressed over 600 Indian American congressman, executives and eminent personalities during the Diwali event.US President Joe Biden celebrated Diwali on Monday at the White House in an event attended by more than 600 eminent Indian Americans, reported news agency PTI.US president Joe Biden during a Diwali celebration at the White House on Monday(AFP)US president Joe Biden during a Diwali celebration at the White House on Monday(AFP)“As President, I have been honoured to host the biggest Diwali receptions ever at the White House. To me, it means a great deal. As Senator, Vice President, and President; South Asian Americans have been key members of my staff, said the US president while addressing Indian American congressmen, officials, and corporate executives, from across the country."
    record = [title, img, descr]
    context["record"] = record
    context["name"] = name
    return render(request, 'dashboard.html', context)

def search(request):
    context = {}
    article = request.POST.get('search')
    record = news_article(article)
    context["record"] = record
    return render(request, 'news.html',context)










# def articles(request):
#     articles = []
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'news/articles.html', context)

# def category_articles(request, category_name):
#     category = ["Business", "Health", "Cricket","Football", "Science", "Education", "Technology"]
#     articles = []
#     context = {
#         'category': category,
#         'articles': articles,
#     }
#     return render(request, 'news/category_articles.html', context)



def saved(request):
    id0 = list(request.POST.getlist("list"))
    
    for i in id0:
        i_title = f'title_{i}'
        title = request.POST.get(i_title)
        i_des = f'des_{i}'
        des = request.POST.get(i_des)
        i_link = f'link_{i}'
        link = request.POST.get(i_link)
        val = (id, title, des, link)
        sql = "%s,%s,%s,%s"
        inserting("bookmark", sql, val)
    return redirect('dashboard')


def about(request):
    return render(request, 'about.html')



def bookmark(request):
    context={}
    saved = selection_search("bookmark","email",id)
    context["bookmark"] = saved
    return render(request, 'bookmark.html', context)



