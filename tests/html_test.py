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

        extractor = HtmlExtractor(html_content, False, False)
        result = extractor.extract()

        self.assertIsInstance(result, ExtractorResult)
        self.assertIn("Hello World", result.md_content)
        self.assertIn("test@example.com", result.md_content)

    def test_thei_page(self):
        html_content = """
        <!DOCTYPE html>
<html lang="zh-HK">
  <head>
    <meta charset="UTF-8" />
    <title>Test Page</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
      }
      header, footer {
        background-color: #003366;
        color: white;
        padding: 15px 30px;
      }
      header nav a {
        color: white;
        margin-right: 20px;
        text-decoration: none;
      }
      footer {
        font-size: 0.9em;
        text-align: center;
      }
      main {
        padding: 30px;
      }
    </style>
  </head>
  <body>
    <header>
      <h2>THEi 设计与建筑系</h2>
      <nav>
        <a href="#">主页</a>
        <a href="#">课程</a>
        <a href="#">师资</a>
        <a href="#">设施</a>
        <a href="#">联系我们</a>
      </nav>
    </header>

    <main>
      <h1>Hello World</h1>
      <p>Email: <a href="mailto:test@example.com">test@example.com</a></p>
    </main>

    <footer>
      Copyright © 2025 Technological and Higher Education Institute of Hong Kong. All rights reserved.
    </footer>
  </body>
</html>
        """

        no_footer = HtmlExtractor(html_content, False, True).extract().md_content
        self.assertNotIn("Copyright", no_footer)
        no_header = HtmlExtractor(html_content, True, False).extract().md_content
        self.assertNotIn("THEi 设计与建筑系", no_header)

if __name__ == '__main__':
    unittest.main()
