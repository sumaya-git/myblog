#python
from django.http import HttpResponse
from .data import POSTS

def list_posts(request):
    response_text = "\n".join([f"Title: {post['title']}\nContent: {post['content']}\n" for post in POSTS])
    return HttpResponse(response_text, content_type='text/plain')

