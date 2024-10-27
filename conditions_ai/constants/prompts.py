"""Constants for all the conditions"""

SYSTEM_PROMPT = """
You are an AI assistant that will help with checking conditions for provided numbers. 
You will return only True or False.
"""

A_GREATER_THAN_B = """
Is number {a} greater than number {b}?
{a} > {b}
"""

A_LESS_THAN_B = """
Is number {a} less than number {b}?
{a} < {b}
"""

A_EQUAL_TO_B = """
Is number {a} equal to number {b}?
{a} == {b}
"""

A_NOT_EQUAL_TO_B = """
Is number {a} not equal to number {b}?
{a} != {b}
"""

A_IS_EVEN = """
Is number {a} even?
{a} % 2 == 0
"""

A_IS_ODD = """
Is number {a} odd?
{a} % 2 != 0
"""

A_IS_POSITIVE = """
Is number {a} positive?
{a} > 0
"""

A_IS_NEGATIVE = """
Is number {a} negative?
{a} < 0
"""

A_IS_ZERO = """
Is number {a} zero?
"""
