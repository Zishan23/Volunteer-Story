from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserModelSerializer
from blog.models import PostModel, CategoryModel, SubCategoryModel


class CategoryModelSerializerMeta(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'title',
        ]


class CategoryModelSerializer:
    class Write(CategoryModelSerializerMeta):
        class Meta(CategoryModelSerializerMeta.Meta):
            fields = CategoryModelSerializerMeta.Meta.fields

    class List(CategoryModelSerializerMeta):
        class Meta(CategoryModelSerializerMeta.Meta):
            fields = CategoryModelSerializerMeta.Meta.fields + [
                'id',
            ]
            read_only_fields = ['id']


class SubCategoryModelSerializerMeta(ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = [
            'category',
            'title',
        ]


class SubCategoryModelSerializer:
    class Write(SubCategoryModelSerializerMeta):
        class Meta(SubCategoryModelSerializerMeta.Meta):
            fields = SubCategoryModelSerializerMeta.Meta.fields

    class List(SubCategoryModelSerializerMeta):
        category = CategoryModelSerializer.List(many=False, read_only=True)

        class Meta(SubCategoryModelSerializerMeta.Meta):
            fields = SubCategoryModelSerializerMeta.Meta.fields + [
                'id',
            ]
            read_only_fields = ['id']


class PostModelSerializerMeta(ModelSerializer):
    class Meta:
        model = PostModel
        fields = [
            'id',
            'title',
            'overview',
            'content',
            'category',
            'sub_category',
            'thumbnail',
            'slug',
        ]


class PostModelSerializer:
    class Write(PostModelSerializerMeta):
        class Meta(PostModelSerializerMeta.Meta):
            fields = PostModelSerializerMeta.Meta.fields

    class List(PostModelSerializerMeta):
        author = UserModelSerializer.Lite(many=False, read_only=True)
        # comment = CommentModelSerializer.Lite(many=True, read_only=True)

        class Meta(PostModelSerializerMeta.Meta):
            fields = PostModelSerializerMeta.Meta.fields + [
                'id',
                'slug',
                'author',
                'created_at',
                'updated_at',
            ]
            read_only_fields = ['id', 'created_at', 'updated_at']
