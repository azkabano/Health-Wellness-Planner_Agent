
from agents import function_tool, RunContextWrapper
from context import UserSessionContext
import asyncio

@function_tool
async def meal_planner_tool(
    wrapper: RunContextWrapper[UserSessionContext],
    dietary_preferences: str = "balanced",
    goal: str = "general health"
) -> str:
    """
Generates a personalized 7-day meal plan based on the user's dietary preferences and health goal.

This tool selects an appropriate meal plan (vegetarian, keto, high-protein, or balanced) 
by matching keywords from the user's dietary input and stores it in the session context. 
It then returns a formatted 7-day schedule tailored to the user's health goal 
(e.g., general health, weight loss, muscle gain).

Note:
    This tool should be called after both dietary_preferences and goal are provided.

Args:
    wrapper (RunContextWrapper[UserSessionContext]): The session context for storing the selected meal plan.
    dietary_preferences (str): User's dietary input (e.g., "balanced", "vegetarian", "keto", "high protein").
    goal (str): User's health goal (e.g., "general health", "weight loss", "muscle gain").

Returns:
    str: A formatted 7-day meal plan as a string with context-aware motivation.
"""

    await asyncio.sleep(1)

    # Define meal plans
    meal_plans = {
        "vegetarian": [
            "Oatmeal with fruits, Veggie wrap, Lentil curry with rice",
            "Greek yogurt with granola, Quinoa salad, Vegetable stir-fry",
            "Smoothie bowl, Caprese sandwich, Chickpea curry",
            "Avocado toast, Buddha bowl, Vegetable pasta",
            "Chia pudding, Hummus wrap, Black bean tacos",
            "Fruit salad, Quinoa soup, Vegetable pizza",
            "Pancakes, Greek salad, Mushroom risotto"
        ],
        "keto": [
            "Eggs with bacon, Chicken salad, Salmon with broccoli",
            "Avocado smoothie, Tuna salad, Beef with asparagus",
            "Cheese omelet, Chicken wings, Pork chops with cauliflower",
            "Bulletproof coffee, Egg salad, Lamb with green beans",
            "Bacon and eggs, Chicken thighs, Steak with spinach",
            "Keto pancakes, Sardines, Turkey with Brussels sprouts",
            "Cheese platter, Chicken soup, Cod with zucchini"
        ],
        "balanced": [
            "Oatmeal with berries, Grilled chicken salad, Salmon with vegetables",
            "Greek yogurt, Turkey sandwich, Lean beef with sweet potato",
            "Smoothie, Quinoa bowl, Grilled fish with rice",
            "Eggs with toast, Chicken wrap, Pasta with vegetables",
            "Cereal with milk, Tuna salad, Chicken with broccoli",
            "Fruit bowl, Veggie burger, Turkey with quinoa",
            "Pancakes, Caesar salad, Grilled chicken with rice"
        ],
        "high protein": [
            "Egg whites and oats, Chicken breast sandwich, Beef stir fry",
            "Protein shake, Tuna salad, Salmon with sweet potato",
            "Scrambled eggs, Quinoa chicken bowl, Turkey meatballs",
            "Cottage cheese, Lentil salad, Grilled steak and beans",
            "Boiled eggs, Chicken Caesar wrap, Grilled tofu and rice",
            "Yogurt and almonds, Beef jerky, High-protein pasta",
            "Pancakes with whey, Chickpea stew, Grilled shrimp bowl"
        ]
    }

    # Select meal plan
    preference_key = dietary_preferences.lower()

    if "vegetarian" in preference_key or "vegan" in preference_key:
        selected_plan = meal_plans["vegetarian"]
        plan_type = "Vegetarian"
    elif "keto" in preference_key or "low carb" in preference_key:
        selected_plan = meal_plans["keto"]
        plan_type = "Keto"
    elif "high protein" in preference_key or "protein" in preference_key:
        selected_plan = meal_plans["high protein"]
        plan_type = "High Protein"
    else:
        selected_plan = meal_plans["balanced"]
        plan_type = "Balanced"

    # Save to context
    wrapper.context.meal_plan = selected_plan

    # Friendly output
    response = f"🍽️ Here's your 7-day {plan_type} meal plan to support your **{goal}** goal:\n"
    for i, meals in enumerate(selected_plan, 1):
        response += f"Day {i}: {meals}\n"

    response += f"\n💡 This plan is tailored for your '{dietary_preferences}' dietary preference and your goal of **{goal}**."
    return response