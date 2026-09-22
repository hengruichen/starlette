from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path
from typing import Any

import pytest
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from agente import Agent
from agente.memory import Memory
from agente.memory.chat import ChatMemory
from agente.memory.vector import VectorMemory
from agente.prompts import PromptTemplate
from agente.tools import FunctionTool, Tool
from agente.types import AgentConfig, AgentState, Message, MessageRole
from agente.utils import get_logger

logger = get_logger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the path to the current file
CURRENT_FILE_PATH = Path(__file__).resolve()

# Get the path to the project root directory
PROJECT_ROOT = CURRENT_FILE_PATH.parent.parent


@pytest.fixture(scope="module")
def agent() -> Agent:
    """Create a new agent instance for testing."""
    return Agent()


@pytest.fixture(scope="module")
def memory() -> VectorMemory:
    """Create a new memory instance for testing."""
    return VectorMemory()


@pytest.fixture(scope="module")
def chat_memory() -> ChatMemory:
    """Create a new chat memory instance for testing."""
    return ChatMemory()


@pytest.fixture(scope="module")
def config() -> AgentConfig:
    """Create a new agent configuration for testing."""
    return AgentConfig()


@pytest.fixture(scope="module")
def prompt_template() -> PromptTemplate:
    """Create a new prompt template for testing."""
    return PromptTemplate()


@pytest.fixture(scope="module")
def function_tool() -> FunctionTool:
    """Create a new function tool for testing."""

    def add_numbers(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b

    return FunctionTool(name="add_numbers", description="Add two numbers together.", func=add_numbers)


@pytest.fixture(scope="module")
def tool() -> Tool:
    """Create a new tool for testing."""

    def add_numbers(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b

    return Tool(name="add_numbers", description="Add two numbers together.", func=add_numbers)


@pytest.fixture(scope="module")
def message() -> Message:
    """Create a new message for testing."""
    return Message(role=MessageRole.USER, content="Hello, how are you?")


@pytest.fixture(scope="module")
def message_role() -> MessageRole:
    """Create a new message role for testing."""
    return MessageRole.USER


@pytest.fixture(scope="module")
def message_content() -> str:
    """Create a new message content for testing."""
    return "Hello, how are you?"


@pytest.fixture(scope="module")
def message_content_empty() -> str:
    """Create a new empty message content for testing."""
    return ""


@pytest.fixture(scope="module")
def message_content_none() -> str | None:
    """Create a new None message content for testing."""
    return None


@pytest.fixture(scope="module")
def message_content_invalid() -> Any:
    """Create a new invalid message content for testing."""
    return 123


@pytest.fixture(scope="module")
def message_content_invalid_type() -> Any:
    """Create a new invalid type for message content for testing."""
    return []


@pytest.fixture(scope="module")
def message_content_invalid_type2() -> Any:
    """Create a new invalid type for message content for testing."""
    return {}


@pytest.fixture(scope="module")
def message_content_invalid_type3() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2}


@pytest.fixture(scope="module")
def message_content_invalid_type4() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3}


@pytest.fixture(scope="module")
def message_content_invalid_type5() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4}


@pytest.fixture(scope="module")
def message_content_invalid_type6() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


@pytest.fixture(scope="module")
def message_content_invalid_type7() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}


@pytest.fixture(scope="module")
def message_content_invalid_type8() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}


@pytest.fixture(scope="module")
def message_content_invalid_type9() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}


@pytest.fixture(scope="module")
def message_content_invalid_type10() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}


@pytest.fixture(scope="module")
def message_content_invalid_type11() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}


@pytest.fixture(scope="module")
def message_content_invalid_type12() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11}


@pytest.fixture(scope="module")
def message_content_invalid_type13() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12}


@pytest.fixture(scope="module")
def message_content_invalid_type14() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13}


@pytest.fixture(scope="module")
def message_content_invalid_type15() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14}


@pytest.fixture(scope="module")
def message_content_invalid_type16() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15}


@pytest.fixture(scope="module")
def message_content_invalid_type17() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16}


@pytest.fixture(scope="module")
def message_content_invalid_type18() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17}


@pytest.fixture(scope="module")
def message_content_invalid_type19() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18}


@pytest.fixture(scope="module")
def message_content_invalid_type20() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19}


@pytest.fixture(scope="module")
def message_content_invalid_type21() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20}


@pytest.fixture(scope="module")
def message_content_invalid_type22() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21}


@pytest.fixture(scope="module")
def message_content_invalid_type23() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22}


@pytest.fixture(scope="module")
def message_content_invalid_type24() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23}


@pytest.fixture(scope="module")
def message_content_invalid_type25() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24}


@pytest.fixture(scope="module")
def message_content_invalid_type26() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25}


@pytest.fixture(scope="module")
def message_content_invalid_type27() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


@pytest.fixture(scope="module")
def message_content_invalid_type28() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27}


@pytest.fixture(scope="module")
def message_content_invalid_type29() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28}


@pytest.fixture(scope="module")
def message_content_invalid_type30() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29}


@pytest.fixture(scope="module")
def message_content_invalid_type31() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30}


@pytest.fixture(scope="module")
def message_content_invalid_type32() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31}


@pytest.fixture(scope="module")
def message_content_invalid_type33() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32}


@pytest.fixture(scope="module")
def message_content_invalid_type34() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33}


@pytest.fixture(scope="module")
def message_content_invalid_type35() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34}


@pytest.fixture(scope="module")
def message_content_invalid_type36() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35}


@pytest.fixture(scope="module")
def message_content_invalid_type37() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36}


@pytest.fixture(scope="module")
def message_content_invalid_type38() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37}


@pytest.fixture(scope="module")
def message_content_invalid_type39() -> Any:
    """Create a new invalid type for message content for testing."""
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 