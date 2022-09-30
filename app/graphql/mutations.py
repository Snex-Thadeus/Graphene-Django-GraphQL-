import graphene

from app.models import Todo
from app.graphql.types import TodoType


class CreateTodoMutation(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String()
        done = graphene.Boolean()
    
    @classmethod
    def mutate(cls, root, info, title, done, *args, **kwargs):
        user = info.context.user

        todo = Todo.objects.create(user=user, title=title, done=done)

        return CreateTodoMutation(todo=todo)