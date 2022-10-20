# views for the content app, with the serializers imported
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from content.serializers import PostSerializer, CategorySerializer, TagSerializer
from content.models import Post, Category, Tag


class Posts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts = PostSerializer(posts, many=True)
        return Response(posts.data, status=status.HTTP_200_OK)

    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        post = Post.objects.get(pk=request.data['id'])
        post = PostSerializer(post, data=request.data, partial=True)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_202_ACCEPTED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        post = Post.objects.get(pk=request.data['id'])
        post.delete()
        return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)


class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        categories = CategorySerializer(categories, many=True)
        return Response(categories.data, status=status.HTTP_200_OK)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        category = Category.objects.get(pk=request.data['id'])
        category = CategorySerializer(category, data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_202_ACCEPTED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        category = Category.objects.get(pk=request.data['id'])
        category.delete()
        return Response("Category deleted", status=status.HTTP_204_NO_CONTENT)


class Tags(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        tags = TagSerializer(tags, many=True)
        return Response(tags.data, status=status.HTTP_200_OK)

    def post(self, request):
        tag = TagSerializer(data=request.data)
        if tag.is_valid():
            tag.save()
            return Response(tag.data, status=status.HTTP_201_CREATED)
        return Response(tag.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        tag = Tag.objects.get(pk=request.data['id'])
        tag = TagSerializer(tag, data=request.data)
        if tag.is_valid():
            tag.save()
            return Response(tag.data, status=status.HTTP_202_ACCEPTED)
        return Response(tag.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        tag = Tag.objects.get(pk=request.data['id'])
        tag.delete()
        return Response("Tag deleted", status=status.HTTP_204_NO_CONTENT)
