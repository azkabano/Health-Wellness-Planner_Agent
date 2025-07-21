
from agents import function_tool, RunContextWrapper
from context import UserSessionContext
import asyncio

@function_tool
async def workout_planner(
    wrapper: RunContextWrapper[UserSessionContext],
    fitness_level: str = "beginner"
) -> str:
    """
Generates a personalized 7-day workout plan based on the user's fitness level.

This tool uses the user's fitness level ("beginner", "intermediate", or "advanced") to create 
a weekly workout schedule and stores it in the user session context. If an unknown fitness level 
is provided, a beginner-level plan is returned by default.

Args:
    wrapper (RunContextWrapper[UserSessionContext]): Context wrapper to access and update user state.
    fitness_level (str): User's current fitness level ("beginner", "intermediate", "advanced").

Returns:
    str: A formatted 7-day workout schedule with motivational tips.
"""

    await asyncio.sleep(1)

    # Weekly workout plans based on levels
    workout_plans = {
        "beginner": [
            "Day 1: 20 min walk + light stretching",
            "Day 2: Rest",
            "Day 3: 15 min yoga + bodyweight squats",
            "Day 4: Rest",
            "Day 5: 10 min cycling + push-ups",
            "Day 6: Light jog",
            "Day 7: Rest"
        ],
        "intermediate": [
            "Day 1: 30 min jog + push-ups",
            "Day 2: Strength training (upper body)",
            "Day 3: Cardio HIIT (20 mins)",
            "Day 4: Rest",
            "Day 5: Strength training (lower body)",
            "Day 6: Cycling or Swimming",
            "Day 7: Yoga"
        ],
        "advanced": [
            "Day 1: Weight lifting + HIIT (30 mins)",
            "Day 2: Sprint intervals + core training",
            "Day 3: Strength training (full body)",
            "Day 4: Active recovery (yoga)",
            "Day 5: Long run (45 mins) + strength",
            "Day 6: Cross-training",
            "Day 7: Mobility & Recovery"
        ]
    }

    # Normalize and select plan
    level = fitness_level.strip().lower()
    selected_plan = workout_plans.get(level, workout_plans["beginner"])
    plan_label = level.title() if level in workout_plans else "Beginner"

    # Save to context
    wrapper.context.workout_plan = {
        "fitness_level": level,
        "weekly_schedule": selected_plan
    }

    # Friendly output
    response = f"💪 Your 7-day workout plan for {plan_label} level:\n\n"
    for i, day_activity in enumerate(selected_plan, 1):
        response += f"{day_activity}\n"
    
    response += "\n📝 Stay consistent, rest well, and hydrate 💧!"
    return response