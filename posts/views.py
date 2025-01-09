#python
#from django.http import HttpResponse
#from .data import POSTS

#def list_posts(request):
#    response_text = "\n".join([f"Title: {post['title']}\nContent: {post['content']}\n" for post in POSTS])
#    return HttpResponse(response_text, content_type='text/plain')

# posts/views.py

from django.http import HttpResponse
from .data import POSTS

def list_posts(request):
    # Count the number of posts
    total_posts = len(POSTS)
    
    # Create the response text
    response_text = f"Total Posts: {total_posts}\n\n"  # Add total count
    response_text += "\n".join(
        [f"Title: {post['title']}\nContent: {post['content']}\n" for post in POSTS]
    )
    
    # Return the response
    return HttpResponse(response_text, content_type='text/plain')
