import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
        # convert_choices_to_enum = False

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    # Note: Graphene automatically camelcases all field names for better compatibility with JavaScript clients.
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)




# query{
#   allIngredients{
#     id
#     name
#   }

# }

# query {
#   categoryByName(name: "Dairy") {
#     id
#     name
#     ingredients {
#       id
#       name
#     }
#   }
# }


# Default QuerySet

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Question

#     @classmethod
#     def get_queryset(cls, queryset, info):
#         if info.context.user.is_anonymous:
#             return queryset.filter(published=True)
#         return queryset


# class Query(graphene.ObjectType):
#     questions = graphene.List(QuestionType)

# def resolve_questions(root, info):
#     # See if a user is authenticated
#     if info.context.user.is_authenticated():
#         return Question.objects.all()
#     else:
#         return Question.objects.none()



#Plain ObjectTypes Defining your customized fields
# class MyQuestion(graphene.ObjectType):
#     text = graphene.String()

# class Query(graphene.ObjectType):
#     question = graphene.Field(MyQuestion, question_id=graphene.String())

#     def resolve_question(root, info, question_id):
#         question = Question.objects.get(pk=question_id)
#         return MyQuestion(
#             text=question.question_text
#         )


#RELAY EXAMPLE
# from graphene import relay
# from graphene_django import DjangoObjectType
# from .models import Question

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Question
#         interfaces = (relay.Node,)  # make sure you add this
#         fields = "__all__"

# class QuestionConnection(relay.Connection):
#     class Meta:
#         node = QuestionType

# class Query:
#     questions = relay.ConnectionField(QuestionConnection)

#     def resolve_questions(root, info, **kwargs):
#         return Question.objects.all()


# You can now execute queries like:

# {
#     questions (first: 2, after: "YXJyYXljb25uZWN0aW9uOjEwNQ==") {
#         pageInfo {
#         startCursor
#         endCursor
#         hasNextPage
#         hasPreviousPage
#         }
#         edges {
#         cursor
#         node {
#             id
#             question_text
#         }
#         }
#     }
# }