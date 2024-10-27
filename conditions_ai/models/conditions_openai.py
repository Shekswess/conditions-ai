"""ConditionsAI module."""

import os
from typing import Union

from dotenv import load_dotenv
from loguru import logger
from openai import OpenAI

from ..constants import prompts
from ..utils.bool_converter import convert_to_bool

load_dotenv()


class ConditionsAIOpenAI:
    """ConditionsAI class using OpenAI API."""

    def __init__(self, openai_model_id: str, openai_api_key: str = None):
        """
        Initialize ConditionsAI class.

        Parameters
        ----------
        openai_model_id : str
            The OpenAI model ID.
        openai_api_key : str, optional
            The OpenAI API key. If not provided, it will be fetched from the environment variable 'OPENAI_API_KEY'.
        """
        if openai_api_key is None:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if openai_api_key is None:
                raise ValueError("OpenAI API key must be provided either as an argument or through the 'OPENAI_API_KEY' environment variable.")

        self.openai_client = OpenAI(api_key=openai_api_key)
        self.openai_model_id = openai_model_id

    def greater_than(self, number_1: int,
                     number_2: int) -> Union[bool, Exception]:
        """Check if number_1 is greater than number_2.

        Parameters
        ----------
        number_1 : int
            The first number.
        number_2 : int
            The second number.

        Returns
        -------
        bool
            True if number_1 is greater than number_2, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is greater than {}", number_1,
                        number_2)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_GREATER_THAN_B.format(
                            a=number_1, b=number_2
                        ),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} > {} is {}", number_1, number_2,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def less_than(self, number_1: int,
                  number_2: int) -> Union[bool, Exception]:
        """Check if number_1 is less than number_2.

        Parameters
        ----------
        number_1 : int
            The first number.
        number_2 : int
            The second number.

        Returns
        -------
        bool
            True if number_1 is less than number_2, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is less than {}", number_1, number_2)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_LESS_THAN_B.format(
                            a=number_1, b=number_2
                        ),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} < {} is {}", number_1, number_2,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def equal_to(self, number_1: int, number_2: int) -> Union[bool, Exception]:
        """Check if number_1 is equal to number_2.

        Parameters
        ----------
        number_1 : int
            The first number.
        number_2 : int
            The second number.

        Returns
        -------
        bool
            True if a is equal to b, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is equal to {}", number_1, number_2)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_EQUAL_TO_B.format(
                            a=number_1, b=number_2
                        ),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} == {} is {}", number_1, number_2,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def not_equal_to(self, number_1: int,
                     number_2: int) -> Union[bool, Exception]:
        """Check if number_1 is not equal to number_2.

        Parameters
        ----------
        number_1 : int
            The first number.
        number_2 : int
            The second number.

        Returns
        -------
        bool
            True if a is not equal to b, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is not equal to {}", number_1,
                        number_2)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_NOT_EQUAL_TO_B.format(
                            a=number_1, b=number_2
                        ),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} != {} is {}", number_1, number_2,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def is_even(self, number: int) -> Union[bool, Exception]:
        """Check if a number is even.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is even, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is even", number)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {"role": "user", "content": prompts.A_IS_EVEN.format(
                        a=number)},
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} is even is {}", number, response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def is_odd(self, number: int) -> Union[bool, Exception]:
        """Check if a number is odd.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is odd, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is odd", number)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {"role": "user", "content": prompts.A_IS_ODD.format(
                        a=number)},
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} is odd is {}", number, response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def is_zero(self, number: int) -> Union[bool, Exception]:
        """Check if a number is zero.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is zero, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is zero", number)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {"role": "user", "content": prompts.A_IS_ZERO.format(
                        a=number)},
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} is zero is {}", number, response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def is_positive(self, number: int) -> Union[bool, Exception]:
        """Check if a number is positive.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is positive, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is positive", number)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_IS_POSITIVE.format(a=number),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} is positive is {}", number,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error

    def is_negative(self, number: int) -> bool:
        """Check if a number is negative.

        Parameters
        ----------
        number : int
            The number to check.

        Returns
        -------
        bool
            True if the number is negative, False otherwise.

        Raises
        ------
        Exception
            If an error occurs.
        """
        try:
            logger.info("Checking if {} is negative", number)
            completion = self.openai_client.chat.completions.create(
                model=self.openai_model_id,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": prompts.A_IS_NEGATIVE.format(a=number),
                    },
                ],
            )
            response = convert_to_bool(completion.choices[0].message.content)
            logger.success("The result of {} is negative is {}", number,
                           response)
            return response
        except Exception as error:
            logger.exception(error)
            return error
