# 일단 serializer 쓰지말고 사용
# from rest_framework import serializers
# from .models import Product, Sales, Comment


# class ProductListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
# class CommentSerializer(serializers.ModelSerializer):
#     # Q 6.
#     # 댓글이 참조하고 있는 게시글 정보 
#     article = ArticleListSerializer(read_only = True)
    
#     class Meta:
#         model = Comment
#         # 댓글 정보에 comment 모두 포함
#         fields = '__all__'


# class ArticleSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True)
#     # Q 11.
#     # 댓글의 수 직렬화
#     comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)
#     class Meta:
#         model = Article
#         fields = '__all__'