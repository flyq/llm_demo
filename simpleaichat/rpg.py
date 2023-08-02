from simpleaichat import AIChat
import orjson
from rich.console import Console
from getpass import getpass

from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field

system_prompt = """You are a world-renowned game master (GM) of tabletop role-playing games (RPGs).

Write a setting description and two character sheets for the setting the user provides.

Rules you MUST follow:
- Always write in the style of 80's fantasy novels.
- All names you create must be creative and unique. Always subvert expectations.
- Include as much information as possible in your response."""

model = "gpt-3.5-turbo-0613"
ai = AIChat(system=system_prompt, model=model, save_messages=False)

response = ai("Python software development and beach volleyball")
print(response)


class player_character(BaseModel):
    name: str = Field(description="Character name")
    race: str = Field(description="Character race")
    job: str = Field(description="Character class/job")
    story: str = Field(description="Three-sentence character history")
    feats: List[str] = Field(description="Character feats")

class write_ttrpg_setting(BaseModel):
    """Write a fun and innovative TTRPG"""

    description: str = Field(
        description="Detailed description of the setting in the voice of the DM"
    )
    name: str = Field(description="Name of the setting")
    pcs: List[player_character] = Field(description="Player characters of the TTRPG")

response_structured = ai(
    "Python software development and beach volleyball", output_schema=write_ttrpg_setting
)

# orjson.dumps preserves field order from the ChatGPT API
print(orjson.dumps(response_structured, option=orjson.OPT_INDENT_2).decode())

input_ttrpg = write_ttrpg_setting.model_validate(response_structured)
