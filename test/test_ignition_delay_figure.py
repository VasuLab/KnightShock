from knightshock.figures import IDTFigure

from numpy.testing import assert_almost_equal


def test_inverse_temperature_axis_limits():
    """Test that scaled temperature limit get/set property matches expected values for the inverse temperature axis."""
    IDT_fig = IDTFigure()
    IDT_fig.T_lim = 1000, 1250
    assert_almost_equal(IDT_fig.ax.get_xlim(), (0.80, 1))
    assert_almost_equal(IDT_fig.T_lim, (1000, 1250))


def test_IDT_axis_limits():
    """Test the IDT limit get/set property."""
    IDT_fig = IDTFigure()
    IDT_fig.IDT_lim = 10, 1000
    assert_almost_equal(IDT_fig.ax.get_ylim(), (10, 1000))
    assert_almost_equal(IDT_fig.IDT_lim, (10, 1000))


def test_units():
    """Test that setting the units results in the correct axis label."""
    IDTFigure.units = "ms"
    IDT_fig = IDTFigure()
    assert IDT_fig.ax.get_ylabel() == r"Ignition Delay Time [$\mathrm{ms}$]"
