from api import models
from rest_framework import serializers


#课程类的序列化

# class DegreeCourseSerializer(serializers.Serializer):
#     class Meta:
#         model = models.DegreeCourse
#         fields = '__all__'
#
# class CourseSerializer(serializers.Serializer):
#     class Meta:
#         model = models.Course
#         fields = "__all__"
# class CourseDetailSerializer(serializers.Serializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = '__all__'
# class CourseSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()

class CourseModelSerializer(serializers.ModelSerializer):
    #source帮助做跨表查询--->ModelSeriliazer  获取只想要的字段，source='表名小写'

    level = serializers.CharField(source='get_level_display', read_only=True)
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommand_course = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    outline = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ["name","level","why_study","what_to_study_brief","recommand_course","outline","chapter","question"]

    def get_recommand_course(self,row):
        recommand_course_list = row.coursedetail.recommend_courses.all()

        return [{recommand_course.name} for recommand_course in recommand_course_list]


    def get_question(self, row):
        question_list = row.asked_question.all()
        print(question_list)
        return [{question1.question:question1.answer} for question1 in question_list]


    def get_outline(self, row):
        outline_list = row.coursedetail.courseoutline_set.all()
        return [{outline.title} for outline in outline_list]

    def get_chapter(self,row):
        chapter_list = row.coursechapters.all()
        return [{chapter.name} for chapter in chapter_list]









