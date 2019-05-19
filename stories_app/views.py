from django.shortcuts import render, get_object_or_404
from .models import Story, News

def home(request):
    #story = get_object_or_404(Story) # Returning only one object for many use get_list_or_404
    #story = Story.objects.latest("id") #getting the most risent by id
    mainStory = Story.objects.order_by("-pub_date")
    #return render(request, 'stories_app/index.html', {'story':story}, {'mainStorys':mainStory})
    return render(request, 'stories_app/index.html', {'mainStorys':mainStory})
# post = get_object_or_404(Post, pk=post_id) # quering the DB with post_id by on eobject
# one object - Entry.objects.get(pk=1)
def stories(request):
    mainStory = Story.objects.order_by("-pub_date")
    return render(request, 'stories_app/stories.html', {'mainStorys':mainStory})


def news(request):
    mainNews = News.objects.order_by("-pub_date")
    return render(request, 'stories_app/news.html', {'mainNews':mainNews})

def story_detailes(request, story_id):
    storyDetailes = get_object_or_404(Story, pk=story_id)
    return render(request, 'stories_app/story_detailes.html', {'storyDetailes':storyDetailes})

def contacts(request):
    return render(request, 'stories_app/contacts.html')

def services(request):
    return render(request, 'stories_app/services.html')

def test(request):
    return render(request, 'stories_app/test.html')
