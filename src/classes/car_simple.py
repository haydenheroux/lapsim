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

    @property
    def mass_car(self) -> float:
        mass_car: float = self.attrs["mass_car"]
        return mass_car

    @property
    def mass_driver(self) -> float:
        mass_driver: float = self.attrs["mass_driver"]
        return mass_driver

    @property
    def proportion_front(self) -> float:
        proportion_front: float = self.attrs["proportion_front"]
        return proportion_front

    @property
    def front_track_width(self) -> float:
        front_track_width: float = self.attrs["front_track_width"]
        return front_track_width

    @property
    def rear_track_width(self) -> float:
        rear_track_width: float = self.attrs["rear_track_width"]
        return rear_track_width

    @property
    def wheelbase(self) -> float:
        wheelbase: float = self.attrs["wheelbase"]
        return wheelbase

    @property
    def CG_height(self) -> float:
        CG_height: float = self.attrs["CG_height"]
        return CG_height

    @property
    def yaw_inertia(self) -> float:
        yaw_inertia: float = self.attrs["yaw_inertia"]
        return yaw_inertia

    @property
    def CoF(self) -> float:
        CoF: float = self.attrs["CoF"]
        return CoF

    @property
    def load_sensitivity(self) -> float:
        load_sensitivity: float = self.attrs["load_sensitivity"]
        return load_sensitivity

    @property
    def Cd(self) -> float:
        Cd: float = self.attrs["Cd"]
        return Cd

    @property
    def Cl(self) -> float:
        Cl: float = self.attrs["Cl"]
        return Cl

    @property
    def A(self) -> float:
        A: float = self.attrs["A"]
        return A

    @property
    def rho(self) -> float:
        rho: float = self.attrs["rho"]
        return rho

    @property
    def front_downforce(self) -> float:
        front_downforce: float = self.attrs["front_downforce"]
        return front_downforce

    @property
    def cp_height(self) -> float:
        cp_height: float = self.attrs["cp_height"]
        return cp_height

    @property
    def brake_bias(self) -> float:
        brake_bias: float = self.attrs["brake_bias"]
        return brake_bias

    @property
    def tire_radius(self) -> float:
        tire_radius: float = self.attrs["tire_radius"]
        return tire_radius

    @property
    def gear_ratios(self) -> float:
        gear_ratios: float = self.attrs["gear_ratios"]
        return gear_ratios

    @property
    def max_current(self) -> float:
        max_current: float = self.attrs["max_current"]
        return max_current

    @property
    def max_voltage(self) -> float:
        max_voltage: float = self.attrs["max_voltage"]
        return max_voltage

    @property
    def max_cont_torque(self) -> float:
        max_cont_torque: float = self.attrs["max_cont_torque"]
        return max_cont_torque

    @property
    def max_peak_torque(self) -> float:
        max_peak_torque: float = self.attrs["max_peak_torque"]
        return max_peak_torque

    @property
    def final_drive(self) -> float:
        final_drive: float = self.attrs["final_drive"]
        return final_drive

    @property
    def tractive_efficiency(self) -> float:
        tractive_efficiency: float = self.attrs["tractive_efficiency"]
        return tractive_efficiency

    @property
    def drivetrain_efficiency(self) -> float:
        drivetrain_efficiency: float = self.attrs["drivetrain_efficiency"]
        return drivetrain_efficiency

    @property
    def induced_voltage(self) -> float:
        induced_voltage: float = self.attrs["induced_voltage"]
        return induced_voltage

    @property
    def constant_kv(self) -> float:
        constant_kv: float = self.attrs["constant_kv"]
        return constant_kv


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

    def test_attrs_properties_equal(self):
        attrs_car = Car.from_file(self.RM26_FILE)
        properties_car = Car.from_file(self.RM26_FILE)

        self.assertTrue(attrs_car.attrs["mass_car"] == properties_car.mass_car)
        self.assertTrue(attrs_car.attrs["mass_driver"] == properties_car.mass_driver)
        self.assertTrue(
            attrs_car.attrs["proportion_front"] == properties_car.proportion_front
        )
        self.assertTrue(
            attrs_car.attrs["front_track_width"] == properties_car.front_track_width
        )
        self.assertTrue(
            attrs_car.attrs["rear_track_width"] == properties_car.rear_track_width
        )
        self.assertTrue(attrs_car.attrs["wheelbase"] == properties_car.wheelbase)
        self.assertTrue(attrs_car.attrs["CG_height"] == properties_car.CG_height)
        self.assertTrue(attrs_car.attrs["yaw_inertia"] == properties_car.yaw_inertia)
        self.assertTrue(attrs_car.attrs["CoF"] == properties_car.CoF)
        self.assertTrue(
            attrs_car.attrs["load_sensitivity"] == properties_car.load_sensitivity
        )
        self.assertTrue(attrs_car.attrs["Cd"] == properties_car.Cd)
        self.assertTrue(attrs_car.attrs["Cl"] == properties_car.Cl)
        self.assertTrue(attrs_car.attrs["A"] == properties_car.A)
        self.assertTrue(attrs_car.attrs["rho"] == properties_car.rho)
        self.assertTrue(
            attrs_car.attrs["front_downforce"] == properties_car.front_downforce
        )
        self.assertTrue(attrs_car.attrs["cp_height"] == properties_car.cp_height)
        self.assertTrue(attrs_car.attrs["brake_bias"] == properties_car.brake_bias)
        self.assertTrue(attrs_car.attrs["tire_radius"] == properties_car.tire_radius)
        self.assertTrue(attrs_car.attrs["gear_ratios"] == properties_car.gear_ratios)
        self.assertTrue(attrs_car.attrs["max_current"] == properties_car.max_current)
        self.assertTrue(attrs_car.attrs["max_voltage"] == properties_car.max_voltage)
        self.assertTrue(
            attrs_car.attrs["max_cont_torque"] == properties_car.max_cont_torque
        )
        self.assertTrue(
            attrs_car.attrs["max_peak_torque"] == properties_car.max_peak_torque
        )
        self.assertTrue(attrs_car.attrs["final_drive"] == properties_car.final_drive)
        self.assertTrue(
            attrs_car.attrs["tractive_efficiency"] == properties_car.tractive_efficiency
        )
        self.assertTrue(
            attrs_car.attrs["drivetrain_efficiency"]
            == properties_car.drivetrain_efficiency
        )
        self.assertTrue(
            attrs_car.attrs["induced_voltage"] == properties_car.induced_voltage
        )
        self.assertTrue(attrs_car.attrs["constant_kv"] == properties_car.constant_kv)
