from flask import Blueprint, render_template, request
from app.logic import daily_required_calories, find_sum_or_error_msg


main_page_bp = Blueprint('main_page', __name__)


@main_page_bp.route("/", methods=['GET', 'POST'])
def index():
    """
    Get required params from form fields. Calculate daily required dose of calories
    and calculate current daily food calories. Transfer these values into a template.
    """
    if request.method == 'POST':
        gender = request.form['gender']
        height = float(request.form['height'])
        mass = float(request.form['mass'])
        age = float(request.form['age'])
        food_list = request.form['food'].split("\n")
        calories = daily_required_calories(mass, height, age, gender)
        food = find_sum_or_error_msg(food_list)
        return render_template('index.html', calories=calories, food=food)

    return render_template('create.html')
