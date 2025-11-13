from bs4 import BeautifulSoup

from tools.document import ExtractorResult
from tools.extractor_base import BaseExtractor


class HtmlExtractor(BaseExtractor):
    def __init__(self, html_content: str, remove_header:bool, remove_footer:bool):
        """
        :param html_content: HTML content in str.
        :param remove_header: Remove the header
        :param remove_footer: Remove the footer
        """
        self.content = html_content
        self.remove_header = remove_header
        self.remove_footer = remove_footer

    def extract(self) -> ExtractorResult:
        return ExtractorResult(
            md_content=self._load_as_text(),
        )

    def _load_as_text(self) -> str:
        soup = BeautifulSoup(self.content, "html.parser")

        if self.remove_header:
            for tag in soup.find_all('header'):
                tag.decompose()
        if self.remove_footer:
            for tag in soup.find_all('footer'):
                tag.decompose()

        text = soup.get_text()
        return text.strip() if text else ""
