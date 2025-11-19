from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.html_extractor import HtmlExtractor


class DifyExtractorTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        html_content = tool_parameters.get("html")
        if not html_content:
            raise ValueError("html is required")
        remove_header = tool_parameters.get("header_class")
        remove_footer = tool_parameters.get("footer_class")

        extractor = HtmlExtractor(html_content, remove_header, remove_footer)
        t = extractor.extract().text
        yield self.create_text_message(t)
