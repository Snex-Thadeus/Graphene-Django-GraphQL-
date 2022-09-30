import graphene

from app.graphql.types import TodoType
from app.models import Todo


class AllTodosQuery(graphene.ObjectType):
    all_todos = graphene.List(TodoType, done=graphene.Boolean())

    def resolve_all_todos(self, info, done=None, *args, **kwarg):
        todos = Todo.objects.all()

        if done is not None:
            todos.filter(done=done)
        
        return todos