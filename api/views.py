from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .serializers import StudentSerializer
from .models import Student


# Model Object - Single Student data
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, many=False)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
