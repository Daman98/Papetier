from django.conf.urls import url
from . import views
from . import models
urlpatterns = [
	url(r'^main/$', views.main, name='main'),
	#url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/bytext/$', views.post_new_text, name='post_new'),
	url(r'^post/new/byimage/$', views.post_new_image, name='post_new'),
	url(r'^post/subject/(?P<Subject>[\w]+)/(?P<topic>[\w]+)/(?P<clas>[\w]+)/(?P<diff>[\w]+)/(?P<count>[\w]+)/$', views.subject_view, name='subject-view'),
	url(r'^post/search/$', views.req_new, name='que_new'),
	url(r'^admin/app1/question/(?P<id>[\S]+)/change/(?P<url>[\S]+)/change/$', views.image_Text, name='imgtext'),
	#url(r'^post/img/(?P<Question_Image>[\S]+)$', views.image_Text, name='imgtext'),
	url(r'^post/image/(?P<url>[\S]+)/$', views.image_Text, name='imgtext'),
   ]    
