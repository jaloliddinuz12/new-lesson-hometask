
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Student, Course, Book, Genre
from .serializers import StudentSerializer, StudentSerializerForAdmin, BookSerializer, BookSerializerForAdmin



class StudentListAPIView(ListCreateAPIView):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            students = Student.objects.filter(course_id=course_id)
        else:
            students = Student.objects.all()
        return  students

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StudentSerializerForAdmin
        return StudentSerializer

class StudentRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"
    # lookup_url_kwarg = "student_id"



class BookListAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        if genre_id:
            books = Book.objects.filter(genre_id=genre_id)
        else:
            books = Book.objects.all()
        return books

class BookRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"



# class StudentAPIView(APIView):
#     def get(self, request: Request, pk: int = None):
#         if pk is None:
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data)
#         else:
#             student = get_object_or_404(Student, pk=pk)
#             return Response(StudentSerializer(student).data)
#
#     def post(self, request, pk: int = None):
#         if pk:
#             return Response({"message": "Method POST not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         student = serializer.save()
#         return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request, pk: int = None):
#         if not pk:
#             return Response({"message": "Method PUT not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(data=request.data, instance=student)
#         serializer.is_valid(raise_exception=True)
#         return Response(StudentSerializer(serializer.save()).data)
#
#     def delete(self, request, pk: int = None):
#         if not pk:
#             return Response({"message": "Method DELETE not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         return Response({"message": "Student deleted successful"}, status=status.HTTP_204_NO_CONTENT)