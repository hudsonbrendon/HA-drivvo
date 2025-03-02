"""Custom units for Drivvo integration."""

from enum import StrEnum


class UnitOfFuelEfficiency(StrEnum):
    """Fuel efficiency units."""

    KILOMETERS_PER_LITER = "km/L"
    MILES_PER_GALLON = "mpg"
    LITERS_PER_100_KILOMETERS = "L/100km"
