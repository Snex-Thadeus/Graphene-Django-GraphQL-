import graphene

from app.graphql.queries import AllTodosQuery
from app.graphql.mutations import CreateTodoMutation


class RootQuery(AllTodosQuery,
                graphene.ObjectType):
    pass


class RootMutation(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)



# query{
#   allTodos{
#     title
#     id
#     createdAt
#     done
#   }
# }


#Create
# mutation{
#   createTodo(title: "I am awesome", done:true){
#     todo{
#       title
# 			id
# 			createdAt
# 			done
#         }
#     }
# }
