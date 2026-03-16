"""
String Methods Module
=====================
Comprehensive demonstration of Python string methods, formatting, and manipulation.

Strings in Python are immutable sequences of Unicode characters.
"""

from __future__ import annotations


class StringDemo:
    """
    Demonstrates string creation and basic properties.
    """

    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return f"StringDemo('{self.text}')"

    def __str__(self) -> str:
        return self.text


def create_strings() -> dict[str, str]:
    """
    Demonstrate various ways to create strings.

    Time Complexity: O(n) for string creation
    Space Complexity: O(n) for storing the string
    """
    return {
        "single_quotes": 'Hello',
        "double_quotes": "World",
        "triple_single": '''Multi
line
string''',
        "triple_double": """Also
multi
line""",
        "empty": "",
        "from_int": str(42),
        "from_float": str(3.14),
        "from_list": str([1, 2, 3]),
        "raw_string": r"C:\Users\name",  # Backslashes preserved
        "bytes_decode": b"hello".decode("utf-8"),
        "join_method": "".join(["a", "b", "c"]),
    }


def string_properties() -> dict[str, int | bool]:
    """
    Demonstrate string property accessors.

    Time Complexity: O(1) for len, O(n) for others
    """
    s = "Hello, World!"

    return {
        "length": len(s),
        "first_char": ord(s[0]),  # Unicode code point
        "contains_hello": "Hello" in s,
        "startswith_hello": s.startswith("Hello"),
        "endswith_world": s.endswith("World!"),
        "is_alpha": "Hello".isalpha(),
        "is_digit": "123".isdigit(),
        "is_alnum": "Hello123".isalnum(),
        "is_space": "   ".isspace(),
        "is_lower": "hello".islower(),
        "is_upper": "HELLO".isupper(),
        "is_title": "Hello World".istitle(),
        "is_ascii": "Hello".isascii(),
    }


def case_methods() -> dict[str, str]:
    """
    Demonstrate string case manipulation methods.

    Time Complexity: O(n) for all methods
    Space Complexity: O(n) - new string returned
    """
    s = "Hello, World!"

    return {
        "upper": s.upper(),
        "lower": s.lower(),
        "capitalize": "hello world".capitalize(),
        "title": "hello world".title(),
        "swapcase": s.swapcase(),
        "casefold": "HELLO".casefold(),  # More aggressive lower
    }


def search_methods() -> dict[str, int | bool | str]:
    """
    Demonstrate string search methods.

    Time Complexity: O(n*m) worst case for search, O(n) for simple operations
    """
    s = "Hello, World! Hello!"

    return {
        "find_hello": s.find("Hello"),      # Returns -1 if not found
        "find_python": s.find("Python"),    # -1
        "rfind_hello": s.rfind("Hello"),    # Search from right
        "index_hello": s.index("Hello"),    # Raises ValueError if not found
        "count_hello": s.count("Hello"),
        "count_o": s.count("o"),
        "replace_hello": s.replace("Hello", "Hi"),
        "replace_first": s.replace("Hello", "Hi", 1),  # Only first occurrence
    }


def strip_methods() -> dict[str, str]:
    """
    Demonstrate string stripping methods.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return {
        "strip": "  hello  ".strip(),
        "lstrip": "  hello  ".lstrip(),
        "rstrip": "  hello  ".rstrip(),
        "strip_chars": "xxhelloxx".strip("x"),
        "strip_multiple": "abchelloabc".strip("abc"),
        "removeprefix": "HelloWorld".removeprefix("Hello"),
        "removesuffix": "HelloWorld".removesuffix("World"),
    }


def split_methods() -> dict[str, list[str]]:
    """
    Demonstrate string splitting methods.

    Time Complexity: O(n)
    Space Complexity: O(n) for result list
    """
    s = "Hello,World,Python"

    return {
        "split_comma": s.split(","),
        "split_with_max": s.split(",", 1),  # Max 1 split
        "split_whitespace": "a  b\tc\n d".split(),  # Any whitespace
        "splitlines": "line1\nline2\rline3".splitlines(),
        "rsplit": "a.b.c".rsplit(".", 1),  # Split from right
        "partition": "a:b:c".partition(":"),  # Returns (before, sep, after)
        "rpartition": "a:b:c".rpartition(":"),  # From right
    }


def justification_methods() -> dict[str, str]:
    """
    Demonstrate string justification/padding methods.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    s = "hello"

    return {
        "ljust": s.ljust(10),
        "rjust": s.rjust(10),
        "center": s.center(10),
        "ljust_fill": s.ljust(10, "-"),
        "rjust_fill": s.rjust(10, "-"),
        "center_fill": s.center(10, "-"),
        "zfill": "42".zfill(5),  # Zero fill for numbers
        "zfill_negative": "-42".zfill(5),
    }


def encoding_methods() -> dict[str, bytes | str]:
    """
    Demonstrate string encoding/decoding.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    s = "Hello, 世界"

    return {
        "encode_utf8": s.encode("utf-8"),
        "encode_ascii": "Hello".encode("ascii"),
        "decode_utf8": b"Hello".decode("utf-8"),
        "hex": "hello".encode().hex(),
        "from_hex": bytes.fromhex("68656c6c6f").decode(),
    }


def string_formatting() -> dict[str, str]:
    """
    Demonstrate string formatting methods.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    name = "Alice"
    age = 30
    score = 95.5678

    return {
        "f_string": f"Name: {name}, Age: {age}",
        "f_string_expr": f"Sum: {1 + 2}",
        "f_string_format": f"Score: {score:.2f}",
        "f_string_width": f"{name:>10}",
        "format_method": "Name: {}, Age: {}".format(name, age),
        "format_indexed": "Name: {0}, Age: {1}, Again: {0}".format(name, age),
        "format_named": "Name: {n}, Age: {a}".format(n=name, a=age),
        "format_spec": "Score: {:.2f}".format(score),
        "percent_style": "Name: %s, Age: %d" % (name, age),
        "percent_float": "Score: %.2f" % score,
    }


def format_specifications() -> dict[str, str]:
    """
    Demonstrate format specification mini-language.
    """
    num = 42.12345

    return {
        "decimal": f"{num:d}" if isinstance(num, int) else f"{int(num):d}",
        "float_2f": f"{num:.2f}",
        "float_10f": f"{num:10.2f}",
        "scientific": f"{num:e}",
        "scientific_2e": f"{num:.2e}",
        "percentage": f"{0.856:.2%}",
        "binary": f"{42:b}",
        "octal": f"{42:o}",
        "hex_lower": f"{255:x}",
        "hex_upper": f"{255:X}",
        "with_sign": f"{42:+d}",
        "zero_padded": f"{42:05d}",
        "comma_separator": f"{1234567:,}",
        "align_left": f"{'hello':<10}!",
        "align_right": f"{'hello':>10}!",
        "align_center": f"{'hello':^10}!",
    }


def string_concatenation() -> dict[str, str]:
    """
    Demonstrate string concatenation methods.

    Time Complexity: O(n+m) for +, O(n) for join
    """
    a = "Hello"
    b = "World"

    return {
        "plus_operator": a + " " + b,
        "plus_equals": a + b,
        "join": " ".join([a, b]),
        "join_many": ", ".join(["a", "b", "c", "d"]),
        "format": "{} {}".format(a, b),
        "f_string": f"{a} {b}",
        "multiply": "ab" * 3,
    }


def character_operations() -> dict[str, str | int]:
    """
    Demonstrate character-level operations.
    """
    s = "Hello"

    return {
        "first_char": s[0],
        "last_char": s[-1],
        "slice_1_3": s[1:3],
        "reverse": s[::-1],
        "every_other": s[::2],
        "ord_H": ord("H"),
        "chr_72": chr(72),
        "unicode_name": chr(0x1F600),  # 😀
    }


def check_methods() -> dict[str, bool]:
    """
    Demonstrate string check methods.
    """
    return {
        "isalpha": "Hello".isalpha(),
        "isdigit": "123".isdigit(),
        "isalnum": "Hello123".isalnum(),
        "isspace": "   ".isspace(),
        "islower": "hello".islower(),
        "isupper": "HELLO".isupper(),
        "istitle": "Hello World".istitle(),
        "isdecimal": "123".isdecimal(),
        "isnumeric": "①②③".isnumeric(),  # Includes fractions, subscripts
        "isascii": "Hello".isascii(),
        "isprintable": "Hello".isprintable(),
        "isidentifier": "my_var".isidentifier(),
    }


def string_templates() -> dict[str, str]:
    """
    Demonstrate string.Template for simple substitutions.
    """
    from string import Template

    t = Template("Hello, $name! You have $count messages.")

    return {
        "substitute": t.substitute(name="Alice", count=5),
        "safe_substitute": t.safe_substitute(name="Alice"),  # Missing vars kept as-is
        "from_dict": Template("$a + $b = $c").substitute({"a": 1, "b": 2, "c": 3}),
    }


def string_translation() -> dict[str, str]:
    """
    Demonstrate string translation with maketrans/translate.
    """
    table = str.maketrans("abc", "xyz")
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    )

    return {
        "simple_translate": "abc def".translate(table),
        "delete_chars": "hello world".translate(str.maketrans("", "", "aeiou")),
        "rot13": "Hello World".translate(rot13),
    }


if __name__ == "__main__":
    print("=== String Creation ===")
    for name, s in create_strings().items():
        print(f"  {name}: {repr(s)}")

    print("\n=== Case Methods ===")
    for name, s in case_methods().items():
        print(f"  {name}: {s}")

    print("\n=== String Formatting ===")
    for name, s in string_formatting().items():
        print(f"  {name}: {s}")

    print("\n=== Format Specifications ===")
    for name, s in format_specifications().items():
        print(f"  {name}: {s}")

    print("\n=== Split Methods ===")
    for name, result in split_methods().items():
        print(f"  {name}: {result}")
