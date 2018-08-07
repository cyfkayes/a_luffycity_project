
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from api.utils.response import BaseResponse
from api import models

from rest_framework.pagination import PageNumberPagination
from api.serializers.degreecourse import DegreeCourseModelSerializer
from rest_framework.response import Response



# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourse(APIView):

    def get(self, request, *args, **kwargs):

        ret = BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()
            for row in degree_list:
                print(row.name)
                scholarship = row.scholarship_set.all()
                for item in scholarship:
                    print('---->', item.time_percent, item.value)

        except Exception as e:
            ret.code = 500
            ret.error = 'failed to get data'
        return Response(ret.dict)


class DegreeCourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code':1000, 'data':None, 'error':None}
        try:
            degreecourse = models.DegreeCourse.objects.get(id=pk).first()
            ser = DegreeCourseModelSerializer(instance=degreecourse)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = 'failed to get data'
        return Response(response)











