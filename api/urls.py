from django.conf.urls import url, include
from api.views import course,degreecourse


urlpatterns = [
    url(r'course/$', course.CoursesView.as_view()),
    url(r'course/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),
    url(r'degreecourse/(?P<pk>\d+)/$', degreecourse.DegreeCourseDetailView.as_view())
]