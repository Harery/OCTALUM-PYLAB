"""Tests for foundation module - Python basics."""

from __future__ import annotations

import pytest


class TestDataTypes:
    """Tests for Python data type understanding."""

    def test_list_type(self) -> None:
        """Verify list type and operations."""
        my_list: list[int] = [1, 2, 3]
        assert isinstance(my_list, list)
        assert len(my_list) == 3
        assert my_list[0] == 1

    def test_dict_type(self) -> None:
        """Verify dictionary type and operations."""
        my_dict: dict[str, int] = {"a": 1, "b": 2}
        assert isinstance(my_dict, dict)
        assert my_dict["a"] == 1
        assert "b" in my_dict

    def test_set_type(self) -> None:
        """Verify set type and uniqueness."""
        my_set: set[int] = {1, 2, 2, 3}
        assert isinstance(my_set, set)
        assert len(my_set) == 3  # Duplicates removed

    def test_tuple_immutability(self) -> None:
        """Verify tuple is immutable."""
        my_tuple: tuple[int, int, int] = (1, 2, 3)
        assert my_tuple[0] == 1
        with pytest.raises(TypeError):
            my_tuple[0] = 4  # type: ignore


class TestOperators:
    """Tests for Python operators."""

    def test_arithmetic_operators(self) -> None:
        """Verify arithmetic operations."""
        assert 10 + 5 == 15
        assert 10 - 5 == 5
        assert 10 * 5 == 50
        assert 10 / 5 == 2.0
        assert 10 // 3 == 3  # Floor division
        assert 10 % 3 == 1  # Modulo
        assert 2**3 == 8  # Power

    def test_comparison_operators(self) -> None:
        """Verify comparison operations."""
        assert 5 == 5
        assert 5 != 4
        assert 5 > 4
        assert 5 >= 5
        assert 4 < 5
        assert 4 <= 5

    def test_logical_operators(self) -> None:
        """Verify logical operations."""
        assert True and True
        assert not (True and False)
        assert True or False
        assert not False


class TestVariables:
    """Tests for variable understanding."""

    def test_variable_assignment(self) -> None:
        """Verify variable assignment."""
        x = 10
        assert x == 10

        y = x
        assert y == 10

        x = 20
        assert x == 20
        assert y == 10  # y unchanged

    def test_multiple_assignment(self) -> None:
        """Verify multiple assignment."""
        a, b, c = 1, 2, 3
        assert a == 1
        assert b == 2
        assert c == 3

    def test_swap_variables(self) -> None:
        """Verify variable swapping."""
        a, b = 1, 2
        a, b = b, a
        assert a == 2
        assert b == 1
