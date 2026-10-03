from rest_framework import serializers

from .models import Student, Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ["full_name", 'birth_year', 'adress', 'course']
        # exclude = ["image"]
        # depth = 1
        # extra_kwargs = {"image": {'write_only': True}}
        read_only_fields = ["phone_number"]







class StudentSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'birth_year', 'address', 'course']


###-------------  kitiblar uchun ==


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ["title", 'price', 'introduction', 'genre']
        # exclude = ["image"]
        # depth = 1
        # extra_kwargs = {"image": {'write_only': True}}
        read_only_fields = ["introduction"]

class BookSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'introduction', 'price', 'genre']
        #depth = 1
        #exclude = ["price"]













# class StudentSerializer(serializers.Serializer):
#     id = serializers.BigIntegerField(read_only=True)
#     full_name = serializers.CharField(max_length=255)
#     phone_number = serializers.CharField(max_length=13, default="+998991234567")
#     birth_year = serializers.IntegerField(default=2010)
#     image = serializers.ImageField(required=False)
#     address = serializers.CharField(max_length=255)
#     course_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance: Student, validated_data):
#         instance.full_name = validated_data.get("full_name", instance.full_name)
#         instance.phone_number = validated_data.get("phone_number", instance.phone_number)
#         instance.birth_year = validated_data.get("birth_year", instance.birth_year)
#         instance.address = validated_data.get("address", instance.address)
#         instance.course_id = validated_data.get("course_id", instance.course_id)
#         instance.save()
#         return instance