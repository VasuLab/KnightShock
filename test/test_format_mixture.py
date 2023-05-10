"""
Tests for the `knightshock.utils.format_mixture` function.
"""

from knightshock.utils import format_mixture

import pytest


def test_str_species_only():
    """Test that a str with only the species name and no mole fraction will be assigned a mole fraction of unity."""
    assert format_mixture("AR") == {"AR": 1}


def test_str_mixture():
    """Test that a mixture string will be converted to a dict."""
    assert format_mixture("O2: 0.21, N2: 0.79") == {"O2": 0.21, "N2": 0.79}


def test_str_format():
    """Test that a str with extra/missing whitespace and inconsistent capitalization is formatted correctly."""
    assert format_mixture(" O2 : 0.21 , n2:0.79") == {"O2": 0.21, "N2": 0.79}


@pytest.mark.xfail
def test_dict_str_representation():
    """Test that a str representation of a dict is formatted correctly."""
    assert format_mixture("{'O2': 0.21, 'N2': 0.79}") == {"O2": 0.21, "N2": 0.79}


def test_dict_correct_format_unchanged():
    """Test that a correctly formatted mixture dict will be returned unchanged."""
    assert format_mixture({"O2": 0.21, "N2": 0.79}) == {"O2": 0.21, "N2": 0.79}


def test_dict_convert_str_mole_fraction():
    """Test that a mole fraction str will be converted to a float."""
    assert format_mixture({"AR": "1"}) == {"AR": 1.0}


def test_dict_species_format():
    """Test that species in a dict will be correctly formatted."""
    assert format_mixture({" O2 ": 0.21, "n2": 0.79}) == {"O2": 0.21, "N2": 0.79}


def test_raises_type_error():
    """Test that a TypeError is raised when a str or dict is not given."""
    with pytest.raises(TypeError):
        format_mixture(("O2: 0.21", "N2: 0.79"))

