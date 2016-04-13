from django.shortcuts import render, get_object_or_404
from polls.models import User, Chessman

def index(request):
	user_list = User.objects.all().order_by('user_id')[:5]
	context = {'user_list' : user_list}
	return render(request, 'common/index.html', context)


def user_info(request):
	user_data = User.objects.all()
	context = {'user_data' : user_data}
	print '===CONTEXT==='
	print context
	return render(request, 'common/user_info.html', context)


# Create your views here.
