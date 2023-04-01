"""Util to generate id"""

from datetime import datetime


def id_generator() -> str:
    """Generates a unique id"""
    return datetime.now().timestamp().hex()
