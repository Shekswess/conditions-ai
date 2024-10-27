"""Tests for the ConditionsAIOpenAI class."""
import os
from conditions_ai.models.conditions_openai import ConditionsAIOpenAI

MODEL_ID = "gpt-4o-mini"
API_KEY = os.getenv("OPENAI_API_KEY")


def test_greater_than():
    """Test the greater_than method with a simple comparison."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.greater_than(5, 3)
    assert result is True, "Expected 5 to be greater than 3"


def test_less_than():
    """Test the less_than method with a simple comparison."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.less_than(3, 5)
    assert result is True, "Expected 3 to be less than 5"


def test_equal_to():
    """Test the equal_to method with equal values."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.equal_to(5, 5)
    assert result is True, "Expected 5 to be equal to 5"


def test_not_equal_to():
    """Test the not_equal_to method with different values."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.not_equal_to(5, 3)
    assert result is True, "Expected 5 to be not equal to 3"


def test_is_even():
    """Test the is_even method with an even number."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.is_even(4)
    assert result is True, "Expected 4 to be even"


def test_is_odd():
    """Test the is_odd method with an odd number."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.is_odd(3)
    assert result is True, "Expected 3 to be odd"


def test_is_zero():
    """Test the is_zero method with zero."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.is_zero(0)
    assert result is True, "Expected 0 to be zero"


def test_is_positive():
    """Test the is_positive method with a positive number."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.is_positive(5)
    assert result is True, "Expected 5 to be positive"


def test_is_negative():
    """Test the is_negative method with a negative number."""
    conditions_ai = ConditionsAIOpenAI(openai_model_id=MODEL_ID,
                                       openai_api_key=API_KEY)
    result = conditions_ai.is_negative(-5)
    assert result is True, "Expected -5 to be negative"
