# 🧠 Health & Wellness Planner Agent (CLI Version)

A smart and friendly **Command-Line AI assistant** that helps you define health goals, plan meals, recommend workouts, schedule check-ins, and track progress — all in one seamless interaction.  
Built with ❤️ using the **OpenAI Agents SDK**.

---

## 🚀 Features

- ✅ **Goal Analyzer** – Parses natural language goals (e.g., _"I want to lose 2 kg in 1 month"_)
- 🥗 **Meal Planner** – Diet plans for various preferences (vegetarian, keto, balanced, high protein.)
- 🏃 **Workout Recommender** – 7-day custom workout plans for beginner, intermediate, or advanced levels
- ⏰ **Check-in Scheduler** – Weekly check-in scheduling with reminders
- 📊 **Progress Tracker** – Logs updates like weight, diet logs, and progress milestones
- 🩹 **Injury Support Agent** – Suggests safe workouts when injured
- 🧑‍⚕️ **Nutrition Expert Agent** – Provides dietary advice for medical or special needs
- 🆘 **Escalation Agent** – Escalates serious or sensitive health concerns to a human coach

---

## 📦 Requirements

- Python `3.8+`
- Gemini API Key (`gemini-2.0-flash` recommended)
- `openai-agents` SDK
- Other dependencies: `pydantic`, `python-dotenv`, etc.

---

# 🔧 Installation

## 1. Clone the Repository
```bash
git clone azkabano/Health-Wellness-Planner_Agent
cd health_wellness_agent
```
---
## 2. Create Virtual Environment
```bash
python -m venv .venv
```
### Activate the virtual environment:
### Windows

```bash
.venv\Scripts\activate
```
### macOS/Linux

```bash
source .venv/bin/activate
```
---
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---
## 4. Add Environmental Variable
Create a .env file in the root of the project:
ini
OPENAI_API_KEY=your-api-key-here
GEMINI_API_KEY = your-api-key-here
--
### ▶️ Run the Agent (CLI)
```bash
python main.py
```
## 💬 Example Conversation
```pgsql
🧠 Welcome to your Health & Wellness Planner!
Type your goals, health info, or meal/workout requests. Type 'exit' to quit.
User Interaction Flow:
```
```yaml
👤 You: I want to lose 2 kg in 1 month  
🤖 AI: Got it! You've set a goal to lose 2 kg in 1 month.

👤 You: I follow a vegetarian diet  
🤖 AI: Here's a weekly vegetarian meal plan...

👤 You: I’m a beginner at workouts  
🤖 AI: Here's your 7-day beginner workout routine...

👤 You: I have neck pain  
🤖 AI: 🩹 I recommend gentle, low-impact workouts like yoga or light walking.

👤 You: Schedule my check-in on Monday at 8am  
🤖 AI: ✅ Check-in set for Monday at 8am.
```

## 🧱 Project Structure
```bash
health_and_wellness_planner_agent/
├── agent/                        # Main agent + sub-agents
│   ├── escalation_agent.py
│   ├── injury_support_agent.py
│   ├── nutrition_expert_agent.py
│
├── tools/                        # Tool implementations
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── scheduler.py
│   ├── tracker.py
│   ├── workout_recommender.py
│
├── context.py                    # Shared context (UserSessionContext, RunContextWrapper)
├── utils/streamin.py             # Streaming, logging, and helper functions
│
├── main.py                       # CLI entry point
├── .env                          # API Key (never commit this)
└── README.md                     # This file
```

### 🔗 Resources
- [OpenAI Agents SDK Documentation](https://platform.openai.com/docs/assistants)
- [Pydantic Docs](https://docs.pydantic.dev)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
