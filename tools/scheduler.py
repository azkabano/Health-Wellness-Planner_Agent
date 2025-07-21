
from agents.tool import function_tool
from pydantic import BaseModel
from typing import Literal
from agents import RunContextWrapper
from context import UserSessionContext

# Input model for check-in time
class CheckinInput(BaseModel):
    day_of_week: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    time_of_day: str  # e.g. "9am", "18:00", etc.

# Output confirmation message
class CheckinConfirmation(BaseModel):
    message: str

# Tool to store user check-in schedule
@function_tool("CheckinSchedulerTool")
async def checkin_scheduler_tool(
    wrapper: RunContextWrapper[UserSessionContext],
    inputs: CheckinInput
) -> CheckinConfirmation:
    """Schedule a user check-in time by saving the day and time to the session context.

    Args:
        wrapper: Contains the current user session context.
        inputs: A structured input with the day of the week and time of day.

    Returns:
        CheckinConfirmation: A confirmation message indicating the scheduled check-in.

    Side Effects:
        Updates `checkin_schedule` in the user context with the provided time and day.
    """
    # If context is empty, initialize the list
    if not wrapper.context.checkin_schedule:
        wrapper.context.checkin_schedule = []

    # Save the check-in info to session context
    wrapper.context.checkin_schedule.append({
        "day": inputs.day_of_week,
        "time": inputs.time_of_day
    })

    # Return a confirmation message
    return CheckinConfirmation(
        message=f"Check-in scheduled for {inputs.day_of_week} at {inputs.time_of_day}."
    )