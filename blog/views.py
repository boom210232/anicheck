from django.shortcuts import render
from django.http import HttpResponse
import blog.models
import asyncio
import nest_asyncio
nest_asyncio.apply()
# from blog.models import *
# Create your views here.

def index(request):
    return render(request, 'blog/blog_index.html', )


def about(request, num):
    return HttpResponse(f"This is a test of Django framework number: {num}")

async def kitsu(request, title):
    if title == None:
        return HttpResponse("กรอกด้วยไอสัส")
    loop = asyncio.get_event_loop()
    loop.create_task(blog.models.anime_search(title))
    # print(blog.models.api_uses(title))
    data = loop.run_until_complete(asyncio.gather(blog.models.anime_search(title)))[0]
    print(data)
    return render(request, 'blog/show_detail.html', context={
        "sub_type" : data[next(iter(data))]['sub-type'],
        "status" : data[next(iter(data))]['status'],
        "synopsis" : data[next(iter(data))]['synopsis'],
        "episode" : data[next(iter(data))]['episode'],
        "age_rating" : data[next(iter(data))]['age-rating'],
        "popularity" : data[next(iter(data))]['popularity'],
        "rating" : data[next(iter(data))]['rating'],
        # "start_at" : data[next(iter(data))]['start_at'],
        # "ended_at" : data[next(iter(data))]['ended_at']
    })

def test_kit():
    return blog.models.api_uses('naruto')

# def about(request):
#     return HttpResponse("This is a test of Django framework")


def result_demo(request):
    return render(request, 'blog/show_detail.html', )
