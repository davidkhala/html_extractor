import re

from bs4 import BeautifulSoup

from tools.document import ExtractorResult
from tools.extractor_base import BaseExtractor


class HtmlExtractor(BaseExtractor):
    def __init__(self, html_content: str, remove_header: str, remove_footer: str):
        """
        :param html_content: HTML content in str.
        :param remove_header: header classes to be removed
        :param remove_footer: footer classes to be removed
        """
        self.content = html_content
        self.remove_header = remove_header
        self.remove_footer = remove_footer

    def extract(self) -> ExtractorResult:
        return ExtractorResult(
            text=self._load_as_text(),
        )

    @staticmethod
    def class_remover(soup, classes_str):
        class_list = [cls.strip() for cls in classes_str.split(',') if cls.strip()]
        if class_list:
            for tag in soup.find_all(True):
                if not tag.attrs:
                    continue
                tag_classes = tag.get('class', [])
                if any(cls in tag_classes for cls in class_list):
                    tag.decompose()

    def _load_as_text(self) -> str:
        soup = BeautifulSoup(self.content, "html.parser")

        if self.remove_header:
            for tag in soup.find_all('header'):
                tag.decompose()
            HtmlExtractor.class_remover(soup, self.remove_header)
        if self.remove_footer:
            for tag in soup.find_all('footer'):
                tag.decompose()
            HtmlExtractor.class_remover(soup, self.remove_footer)

        text = soup.get_text(separator='\n')
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip() if text else ""
