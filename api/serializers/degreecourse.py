from api import models
from rest_framework import serializers
from api.models import DegreeCourse


#
# class CourseSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()

class DegreeCourseModelSerializer(serializers.ModelSerializer):
    #source帮助做跨表查询--->ModelSeriliazer  获取只想要的字段，source='表名小写'

    # level_name = serializers.CharField(source = 'get_level_display')
    # hours = serializers.CharField(source='coursedetail.hours')
    # course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    #
    # recommend_courses = serializers.SerializerMethodField()
    #
    # class Meta:
    #     models = models.Course
    #     fields = ['id','name','level','hours','course_slogan','recommend_courses']
    #
    # def get_recommend_courses(self,row):
    #     recommend_list = row.coursedetail.recommend_courses.all()
    #     return [{'id':item.id,'name':item.name} for item in recommend_list]


    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name','teachers','scholarship']

    def get_teachers(self, row):

        teacher_list = row.teachers.all()
        return [{teacher.name} for teacher in teacher_list]

    def get_scholarship(self, row):

        scholarship_list = row.scholarship_set.all()
        return [{scholarship.value} for scholarship in scholarship_list]



