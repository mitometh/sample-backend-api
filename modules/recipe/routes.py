from flask import Blueprint, jsonify, request, current_app
from modules.recipe.models import Recipe
from modules.common.resp import Response

recipe_api = Blueprint('recipe_api', __name__)

@recipe_api.route('/', methods=['GET'])
def get_recipes():
    try:
        items = Recipe.query.filter_by(deleted=False).order_by(Recipe.updated_at.desc()).limit(10).all()

        current_app.logger.info("Fetched top 10 recipes")

        return jsonify({
            "recipes": [recipe.to_dict() for recipe in items]
        })
    except Exception as e:
        return Response.return_internal_error(e)

@recipe_api.route('/', methods=['POST'])
def create_recipe():
    try:
        data = request.json
        new_recipe = Recipe(
            title=data.get('title'),
            making_time=data.get('making_time'),
            serves=data.get('serves'),
            ingredients=data.get('ingredients'),
            cost=data.get('cost')
        )
        new_recipe.save()
        current_app.logger.info("Recipe {id} created".format(id=new_recipe.id))

        return jsonify({
            "message": "Recipe successfully created!",
            "recipe": [new_recipe.to_dict(True)]
        })
    except ValueError as e:
        return jsonify({
            "message": "Recipe creation failed!",
            "required": "title, making_time, serves, ingredients, cost"
        })

    except Exception as e:
        return Response.return_internal_error(e)

@recipe_api.route('/<int:id>', methods=['GET'])
def get_recipe(id):
    try:
        recipe = Recipe.query.get(id)
        if(recipe and recipe.deleted == False):
            resp = {
                "message": "Recipe details by id",
                "recipe": [recipe.to_dict()]
            }
            return jsonify(resp)
        
        return Response.return_error("No recipe found", 404)
    except Exception as e:
        return Response.return_internal_error(e)
    
@recipe_api.route('/<int:id>', methods=['PATCH'])
def update_recipe(id):
    try:
        data = request.json
        recipe = Recipe.query.get(id)
        if(recipe and recipe.deleted == False):
            recipe.update(data)
            current_app.logger.info("Recipe {id} updated".format(id=recipe.id))

            return jsonify({
                "message": "Recipe successfully updated!",
                "recipe": [recipe.to_dict()]
            })
            
        return Response.return_error("No recipe found", 404)
    
    except ValueError as e:
        return jsonify({
            "message": "Recipe update failed!",
            "required": "title, making_time, serves, ingredients, cost"
        })
    
    except Exception as e:
        return Response.return_internal_error(e)


@recipe_api.route('/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    try:
        recipe = Recipe.query.get(id)
        if(recipe and recipe.deleted == False):
            recipe.delete()

            current_app.logger.info("Recipe {id} removed".format(id=recipe.id))
            
            return jsonify({
                "message":  "Recipe successfully removed!"
            })
        
        return Response.return_error("No recipe found", 404)
    except Exception as e:
        return Response.return_internal_error(e)