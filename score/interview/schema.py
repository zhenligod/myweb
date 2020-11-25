import graphene
from interview import DjangoObjectType
from interview.models import Questions
from interview.models import Staff_Exams
from interview.models import Staff_Exam_Questions

class ExamType(DjangoObjectType):
    class Meta:
        model = Staff_Exams
        fields = ("id", "type", "created_at")

class ExamQuestionType(DjangoObjectType):
    class Meta:
        model = Staff_Exam_Questions
        fields = ("id", "exam_id", "created_at", "is_passed")

class Query(graphene.ObjectType):
    all_exams = graphene.List(ExamType)
    exam_by_staff = graphene.Field(ExamType, name=graphene.String(required=True))

    def resolve_all_exams(root, info):
        # We can easily optimize query count in the resolve method
        return Staff_Exams.objects.select_related("Staff_Exams").all()

    def resolve_exams_by_name(root, info, staff_id):
        try:
            return Staff_Exams.objects.get(staff_id=staff_id)
        except Staff_Exams.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)