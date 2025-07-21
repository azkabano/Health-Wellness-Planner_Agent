
from typing import TypedDict
from agents.tool import function_tool
from datetime import datetime

class ProgressUpdateDict(TypedDict):
    status: str
    user_id: int
    update: str
    timestamp: str
    category: str
    motivational_message: str

@function_tool("progress_tracker_tool")
def progress_tracker(user_id: int, update: str) -> ProgressUpdateDict:
    """
    Tracks and categorizes user progress updates with a motivational response.

    This tool analyzes a user's text-based progress update (e.g., about weight, workouts, or wellness)
    and returns structured feedback including category, timestamp, and a motivational message.

    Args:
        user_id (int): The unique ID of the user submitting the update.
        update (str): A brief description of the user's progress.

    Returns:
        ProgressUpdateDict: A dictionary containing the update status, category,
        motivational message, and timestamp.

    Raises:
        ValueError: If the update is too short or empty.
    """
    if not update or len(update.strip()) < 3:
        raise ValueError("Please provide a valid progress update.")

    text = update.lower()

    if any(word in text for word in ["weight", "lost", "gain"]):
        category = "weight"
        message = "👍 Great job on your weight progress!"
    elif any(word in text for word in ["workout", "gym", "run"]):
        category = "fitness"
        message = "🏃‍♀️ You're crushing your workouts!"
    elif any(word in text for word in ["diet", "meal", "food"]):
        category = "nutrition"
        message = "🥗 Nice work staying on track with your nutrition!"
    elif any(word in text for word in ["sleep", "mood", "energy"]):
        category = "wellness"
        message = "🧘 Your wellness matters. Keep going!"
    else:
        category = "general"
        message = "👏 Thanks for the update. Keep it up!"

    return {
        "status": "progress updated",
        "user_id": user_id,
        "update": update,
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "motivational_message": message
    }