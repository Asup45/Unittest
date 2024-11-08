import unittest

import object_type

class Test_Object_type(unittest.TestCase):
    def test_vehicle_is_instance_of_car(self):
        car = object_type.Car("Chevrolet", "Corvette", 194)
        self.assertIsInstance(car, object_type.Car)

    def test_vehicle_is_instance_of_truck(self):
        truck = object_type.Truck("Ford", "F-150", 2000)
        self.assertIsInstance(truck, object_type.Truck)

    def test_object_type_factory(self):
        car = object_type.vehicle_factory(
            object_type.Car,
            make="Toyota",
            model="Corolla",
            max_speed=180,
        )
        self.assertIsInstance(car, object_type.Vehicle)

if __name__ == "__main__":
    unittest.main(verbosity=2)