from django.http import HttpResponse,JsonResponse
def Home_page(request):
    friends=[
        "ali",
        "ahmad",
        "akbar",
    ]
    print("THIS IS HOME PAGE")
    return JsonResponse(friends,safe=False)
    return HttpResponse('<h1>this is home page</h1>')
