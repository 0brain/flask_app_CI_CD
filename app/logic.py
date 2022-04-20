import os
from typing import Union, List
import requests
import logging


def daily_required_calories(mass: float,
                            height: float,
                            age: float,
                            gender: str) -> float:
    """
    Returns the daily required amount of calories depending on the parameters of the human body.
    The original Harris–Benedict equation used to calculate Basal Metabolic Rate.
    """
    const = 0
    if gender == 'male':
        mass *= 13.7516
        height *= 5.0033
        age *= 6.7550
        const = 66.4730
    elif gender == 'female':
        mass = 9.5634
        height = 1.8496
        age = 4.6756
        const = 655.0955

    p = mass + height - age + const
    return p


def item_search(ingr: str) -> Union[float, str]:
    """
    Returns amount of calories depending on the type of food or 'not in database' message.
    """
    app_id = os.environ.get('APP_ID')
    app_key = os.environ.get('APP_KEY')
    res = requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}\
                         &ingr={ingr}&nutrition-type=cooking")
    try:
        data = res.json()["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"]
    except Exception as e:
        logging.exception(e)
        data = f"Sorry, {ingr} not in database!"
    return data


def find_sum_or_error_msg(food_list: List[str]) -> Union[float, str]:
    """
    Returns sum calories of all food in a list or 'not in database' message.
    """
    total = 0
    for item in food_list:
        kcals = item_search(item)
        if isinstance(kcals, str):
            return kcals
        else:
            total += kcals
    return total
