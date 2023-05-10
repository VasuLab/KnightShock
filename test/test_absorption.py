from knightshock.absorption import *

from numpy.testing import assert_almost_equal


class TestSingleSpecies:

    A = 0.02446355
    sigma = 1e-20  # [cm^2/molecule]
    X = 0.1
    T = 300  # [K]
    P = 101325  # [Pa]
    L = 1  # [cm]

    def test_absorbance(self):
        """Test absorbance calculations."""
        assert_almost_equal(
            absorbance(self.X, self.sigma, self.T, self.P, self.L),
            self.A
        )

    def test_absorption_cross_section(self):
        """Test absorption cross-section calculations."""
        assert_almost_equal(
            absorption_cross_section(self.A, self.X, self.T, self.P, self.L),
            self.sigma
        )

    def test_species_mole_fraction(self):
        """Test species mole fraction calculations."""
        assert_almost_equal(
            species_mole_fraction(self.A, self.sigma, self.T, self.P, self.L),
            self.X
        )

