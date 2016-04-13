"""MCNTacticsServer URL Configuration

The `urlpatterns` list routes URLs to viewss. For more information please see:
	 https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function viewss
	 1. Add an import:  from my_app import viewss
	 2. Add a URL to urlpatterns:  url(r'^$', viewss.home, name='home')
Class-based viewss
	 1. Add an import:  from other_app.viewss import Home
	 2. Add a URL to urlpatterns:  url(r'^$', Home.as_views(), name='home')
Including another URLconf
	 1. Import the include() function: from django.conf.urls import url, include
	 2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from polls import views


urlpatterns = [
	
	url(r'^common/$', views.index, name = 'index'),
	url(r'^common/user_info/$', views.user_info, name = 'user_info'),
	# url(r'^polls/(?P<user_id>\d+)/vote/$', views.vote, name = 'vote'),
	# url(r'^polls/(?P<user_id>\d+)/result/$', views.result, name = 'result'),
	url(r'^admin/', admin.site.urls),
]
