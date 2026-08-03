from pymonad.tools import curry


@curry(2)
def tag(tag_name, value, attr=None):
    attributes = ""

    if attr:
        attributes = " " + " ".join(
            f'{name}="{attribute_value}"'
            for name, attribute_value in attr.items()
        )

    return f"<{tag_name}{attributes}>{value}</{tag_name}>"


bold = tag("b")
italic = tag("i")


def main():
    print(tag("b", "string"))
    print(bold("important"))
    print(italic("emphasis"))
    print(
        tag(
            "li",
            "item 23",
            {"class": "list-group", "id": "item-23"},
        )
    )


if __name__ == "__main__":
    main()
