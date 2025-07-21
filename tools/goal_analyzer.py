
from agents import function_tool, RunContextWrapper
from context import UserSessionContext
import re


@function_tool
async def analyze_health_goal(
    wrapper: RunContextWrapper[UserSessionContext],
    goal_description: str
) -> str:
    """Extract structured details from a health goal description, such as goal type 
    (e.g., weight_loss), target amount (e.g., 5), unit (e.g., kg), and timeframe 
    (e.g., 2 months).

    Stores the extracted info in user context for use in personalized planning.

    Args:
        wrapper: Contains the user context to save the parsed goal.
        goal_description: User's natural language health goal input.

    Returns:
        A user-friendly summary of the analyzed goal.
    """

    # Normalize input
    text = goal_description.lower()

    # Keywords for goal type detection
    weight_loss_keywords = ['lose', 'weight', 'slim', 'diet', 'fat']
    muscle_gain_keywords = ['gain', 'muscle', 'bulk', 'strong', 'build muscle']
    fitness_keywords = ['fit', 'exercise', 'cardio', 'run', 'endurance', 'stamina']
    general_keywords = ['health', 'wellness', 'healthy', 'lifestyle']

    # Detect goal type
    if any(word in text for word in weight_loss_keywords):
        goal_type = "weight_loss"
    elif any(word in text for word in muscle_gain_keywords):
        goal_type = "muscle_gain"
    elif any(word in text for word in fitness_keywords):
        goal_type = "fitness"
    elif any(word in text for word in general_keywords):
        goal_type = "general_health"
    else:
        goal_type = "unspecified"

    # Extract target amount + unit (e.g. 5 kg)
    match_amount_unit = re.search(r'(\d+\.?\d*)\s*(kg|kilograms|lbs|pounds|reps|minutes|hours)?', text)
    target_amount = match_amount_unit.group(1) if match_amount_unit else None
    target_unit = match_amount_unit.group(2) if match_amount_unit and match_amount_unit.group(2) else None

    # Extract timeframe (e.g. "in 2 months")
    match_timeframe = re.search(r'(\d+)\s*(day|week|month|year)s?', text)
    timeframe = f"{match_timeframe.group(1)} {match_timeframe.group(2)}{'s' if int(match_timeframe.group(1)) > 1 else ''}" if match_timeframe else None

    # Build structured goal object
    structured_goal = {
        "goal_type": goal_type,
        "target_amount": target_amount,
        "target_unit": target_unit,
        "timeframe": timeframe,
        "specific_goal": goal_description.strip()
    }

    # Save to user context
    wrapper.context.goal = structured_goal

    # Friendly output
    response = (
        f"🎯 Goal Analyzed:\n"
        f"- Type: {goal_type.replace('_', ' ').title()}\n"
        f"- Target: {target_amount or 'Not specified'} {target_unit or ''}\n"
        f"- Timeframe: {timeframe or 'Flexible'}\n\n"
        f"✅ Let's start building your personalized wellness plan!"
    )

    return response