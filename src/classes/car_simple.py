import json
from typing import Any
import unittest


class Car:
    def __init__(self, attrs: dict[str, Any]):
        self.attrs = attrs

    @classmethod
    def from_file(cls, name: str):
        with open(name) as file:
            attrs: dict[str, Any] = json.load(file)
            return cls(attrs)

    @classmethod
    def from_string(cls, string: str):
        attrs: dict[str, Any] = json.loads(string)
        return cls(attrs)


class TestCar(unittest.TestCase):
    # NOTE: Relative to directory that the test is called from
    RM26_FILE = "app/rm26.json"

    RM26_STRING = """
        {
          "mass_car": 230,
          "mass_driver": 100,
          "proportion_front": 0.5,
          "front_track_width": 1.2319,
          "rear_track_width": 1.19888,
          "wheelbase": 1.6256,
          "CG_height": 0.247556712,
          "yaw_inertia": 100,
          "CoF": 1.6,
          "load_sensitivity": 0.0004077471967,
          "Cd": 1,
          "Cl": 1,
          "A": 1,
          "rho": 1.162,
          "front_downforce": 0.475,
          "cp_height": 0,
          "brake_bias": 0.6,
          "tire_radius": 0.2032,
          "gear_ratios": 2.9,
          "max_current": 250,
          "max_voltage": 399,
          "max_cont_torque": 130,
          "max_peak_torque": 240,
          "final_drive": 2.9,
          "tractive_efficiency": 0.85,
          "drivetrain_efficiency": 0.9,
          "induced_voltage": 0.07348,
          "constant_kv": 10.12
        }
        """

    def test_file_file_equal(self):
        file_car_1 = Car.from_file(self.RM26_FILE)
        file_car_2 = Car.from_file(self.RM26_FILE)

        self.assertTrue(file_car_1.attrs == file_car_2.attrs)

    def test_file_file_modified_not_equal(self):
        file_car_1 = Car.from_file(self.RM26_FILE)
        file_car_2 = Car.from_file(self.RM26_FILE)

        file_car_2.attrs["A"] = 0

        self.assertFalse(file_car_1.attrs == file_car_2.attrs)

    def test_file_string_equal(self):
        file_car = Car.from_file(self.RM26_FILE)
        string_car = Car.from_string(self.RM26_STRING)

        self.assertTrue(file_car.attrs == string_car.attrs)
