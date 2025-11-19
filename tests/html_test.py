import unittest

from tools.document import ExtractorResult
from tools.html_extractor import HtmlExtractor


class ExtractTestCase(unittest.TestCase):
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

        extractor = HtmlExtractor(html_content, "", "-")
        result = extractor.extract()

        self.assertIsInstance(result, ExtractorResult)
        self.assertIn("Hello World", result.text)
        self.assertIn("test@example.com", result.text)

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

        no_footer = HtmlExtractor(html_content, "", "-").extract().text
        self.assertNotIn("Copyright", no_footer)
        no_header = HtmlExtractor(html_content, "-", "").extract().text
        self.assertNotIn("THEi 设计与建筑系", no_header)

    def test_real_page(self):
        with open(
                "fixtures/Bachelor of Engineering (Honours) in Building Services Engineering - Technological and Higher Education Institute of Hong Kong.html",
                'r', encoding='utf-8') as f:
            html_content = f.read()
        header_classes = "mobile-menu-wrapper, breadcrumbs-wrapper, popup-login-wrapper, toolbar"
        footer_classes = 'footer,header-info-swapper,thim-widget-button,elementor-widget-social-icons'
        clean = HtmlExtractor(html_content, header_classes, footer_classes).extract().text
        self.assertNotIn("About", clean)
        self.assertNotIn("Copyright", clean)
        self.assertNotIn("Apply now", clean)
        self.assertIn("ST145103", clean)
        self.assertIn("AECOM Asia Company Limited", clean)
        self.assertIn("Fluid Mechanics", clean)
        self.assertIn("4,230", clean)
        print(clean)


if __name__ == '__main__':
    unittest.main()
