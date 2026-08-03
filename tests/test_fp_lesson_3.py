import unittest

from fp_lesson_3 import bold, italic, tag


class HtmlTagLessonTest(unittest.TestCase):
    def test_tag_wraps_value_without_attributes(self):
        self.assertEqual(tag("b", "string"), "<b>string</b>")

    def test_bold_and_italic_are_partially_applied(self):
        self.assertEqual(bold("important"), "<b>important</b>")
        self.assertEqual(italic("emphasis"), "<i>emphasis</i>")

    def test_tag_adds_one_attribute(self):
        result = tag("li", "item 23", {"class": "list-group"})

        self.assertEqual(result, '<li class="list-group">item 23</li>')

    def test_tag_adds_multiple_attributes(self):
        result = tag(
            "li",
            "item 23",
            {"class": "list-group", "id": "item-23"},
        )

        self.assertEqual(
            result,
            '<li class="list-group" id="item-23">item 23</li>',
        )

    def test_empty_attributes_do_not_add_extra_space(self):
        self.assertEqual(tag("p", "text", {}), "<p>text</p>")


if __name__ == "__main__":
    unittest.main()
