from flask import Flask, json, render_template, request
import math
app = Flask(__name__)
@app.route('/')
def recipes_app():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    with open('recipes.json','r') as f:
        data = json.load(fp=f)
        recipes = data['recipes']
        total_recipes = len(recipes)

        # Pagination logic
        start = (page - 1) * per_page
        end = start + per_page
        paginated_recipes = recipes[start:end]
        total_pages = math.ceil(total_recipes / per_page)

        # recipes = data['recipes']
        # total_recipes = data['total']
    return render_template(
            'recipes2.html',
            recipes=paginated_recipes,
            total_recipes=total_recipes,
            page=page,
            total_pages=total_pages
        )
    # return render_template('recipes2.html', recipes=recipes, total_recipes=total_recipes)


# NEW DETAILS ROUTE
@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    with open('recipes.json','r') as f:
        data = json.load(f)
        recipes = data['recipes']
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)

    if not recipe:
        return "Recipe not found", 404

    return render_template('recipe_detail.html', recipe=recipe)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

