import graphene

import ingredients.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)


# query {
#   allIngredients {
#     edges {
#       node {
#         id,
#         name
#       }
#     }
#   }
# }


# You can also get each ingredient for each category:
# query {
#   allCategories {
#     edges {
#       node {
#         name,
#         ingredients {
#           edges {
#             node {
#               name
#             }
#           }
#         }
#       }
#     }
#   }
# }


# Or you can get only ‘meat’ ingredients containing the letter ‘e’:

# query {
#   # You can also use `category: "CATEGORY GLOBAL ID"`
#   allIngredients(name_Icontains: "e", category_Name: "Meat") {
#     edges {
#       node {
#         name
#       }
#     }
#   }
# }