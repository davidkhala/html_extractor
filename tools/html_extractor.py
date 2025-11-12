"""Abstract interface for document loader implementations."""

from bs4 import BeautifulSoup  # type: ignore

from tools.extractor_base import BaseExtractor
from tools.document import Document, ExtractorResult


class HtmlExtractor(BaseExtractor):
    """
    Args:
        html_content: HTML content in bytes format.
    """

    def __init__(self, html_content: str):
        """Initialize with file bytes."""
        self._file_bytes = html_content

    def extract(self) -> ExtractorResult:
        text = self._load_as_text()
        return ExtractorResult(
            md_content=text,
        )

    def _load_as_text(self) -> str:
        soup = BeautifulSoup(self._file_bytes, "html.parser")
        text = soup.get_text()
        return text.strip() if text else ""
