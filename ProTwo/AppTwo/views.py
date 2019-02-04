from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(request):
    myDict ={'got':'Winter is coming'}
    return render(request,'AppTwo/index.html',myDict)

# def help(request):
#     help_dict = { 'help':"Help Page is here." }
#     return render(request,'AppTwo/help.html',help_dict)

def users(request):
    user_list = User.objects.order_by('First_Name')
    user_dict = {'user':user_list}
    return render(request,'AppTwo/users.html',user_dict)
