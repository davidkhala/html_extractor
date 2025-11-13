from bs4 import BeautifulSoup

from tools.document import ExtractorResult
from tools.extractor_base import BaseExtractor


class HtmlExtractor(BaseExtractor):
    """
    Args:
        html_content: HTML content in bytes format.
    """

    def __init__(self, html_content: str):
        self.content = html_content

    def extract(self) -> ExtractorResult:
        text = self._load_as_text()
        return ExtractorResult(
            md_content=text,
        )

    def _load_as_text(self) -> str:
        soup = BeautifulSoup(self.content, "html.parser")
        text = soup.get_text()
        return text.strip() if text else ""
