from django.shortcuts import render
from django.http import HttpResponse
 #views.postlist 함수는 db에서 필요한 데이터를 가져와서
 #postlist.html에게 넘겨줘야 함.
def homepage(request):
    return HttpResponse('여기는 홈 페이지')
