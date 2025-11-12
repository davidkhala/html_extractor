import unittest
from pathlib import Path

from tools.document import Document, ExtractorResult
from tools.html_extractor import HtmlExtractor  # 修改为实际路径



class MaskTestCase(unittest.TestCase):
    def test_html_extractor_parses_file(self):
        html_content = """
        <html>
          <head><title>Test Page</title></head>
          <body>
            <h1>Hello World</h1>
            <p>Email: <a href="mailto:test@example.com">test@example.com</a></p>
          </body>
        </html>
        """


        # 调用 HtmlExtractor
        extractor = HtmlExtractor(html_content=html_content)
        result = extractor.extract()

        # 断言结果
        self.assertIsInstance(result, ExtractorResult)
        self.assertIn("Hello World", result.md_content)
        self.assertIn("test@example.com", result.md_content)


if __name__ == '__main__':
    unittest.main()