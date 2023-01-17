from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

from .serializers import StudentSerializer
from .models import Student


# Model Object - Single Student data
def student_detail(request, pk):
    """ detail api using JSONRenderer """
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, many=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


def student_list(request):
    """ list api using JSONRenderer """
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
