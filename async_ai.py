from simpleaichat import AsyncAIChat
from getpass import getpass
import asyncio

ai = AsyncAIChat(console=False)

states = ["Washington", "New Mexico", "Texas", "Mississippi", "Alaska"]

ai_2 = AsyncAIChat(console=False)
for state in states:
    ai_2.new_session(id=state)

tasks = []
for state in states:
    tasks.append(ai_2(f"What is the capital of {state}?", id=state))

# results = await asyncio.gather(*tasks)
# results

tasks = []
for state in states:
    tasks.append(ai_2("When was it founded?", id=state))


# results = await asyncio.gather(*tasks)
# results