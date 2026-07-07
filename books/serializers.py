from rest_framework import serializers
from datetime import date
from .models import Author, Category, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
    def validate_bio(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Length of bio should be min 20")
        return value
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, source='category', queryset=Category.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Day should not be ")
        return value
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author , created = Author.objects.get_or_create(
            name=author_data['name'],
            defaults={'bio':author_data['bio']}
        )
        book = Book.objects.create(author=author, **validated_data)
        return book