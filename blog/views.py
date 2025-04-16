from django.shortcuts import render
# views is used to handle requests and provide a response
# we take the request information and handle it in some way
# then we fetch info (if needed) from database to send to html page
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
