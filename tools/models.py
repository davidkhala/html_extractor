from typing import Optional

from pydantic import BaseModel


class ExtractorResult(BaseModel):
    """Class for storing the result of an extractor."""

    text: str
    files: Optional[list] = None
    json: Optional[list[dict]] = None
