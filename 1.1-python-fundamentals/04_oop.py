"""
Task 1.1 - Python Fundamentals
Topic: Object-Oriented Programming (classes, inheritance, encapsulation, polymorphism)
"""


class Robot:
    """Base class demonstrating encapsulation with a private attribute."""

    total_robots = 0  # class variable shared across instances

    def __init__(self, name, battery_level=100):
        self.name = name
        self._battery_level = battery_level  # "protected" by convention
        Robot.total_robots += 1

    def move(self):
        if self._battery_level <= 0:
            return f"{self.name} cannot move — battery empty."
        self._battery_level -= 10
        return f"{self.name} moved. Battery at {self._battery_level}%."

    def get_battery(self):
        return self._battery_level

    def __str__(self):
        return f"Robot(name={self.name}, battery={self._battery_level}%)"


class DroneRobot(Robot):
    """Subclass demonstrating inheritance and method overriding (polymorphism)."""

    def __init__(self, name, battery_level=100, max_altitude=50):
        super().__init__(name, battery_level)
        self.max_altitude = max_altitude

    def move(self):
        # Overrides Robot.move to consume more battery (flying costs more)
        if self._battery_level <= 0:
            return f"{self.name} cannot fly — battery empty."
        self._battery_level -= 20
        return f"{self.name} flew up to {self.max_altitude}m. Battery at {self._battery_level}%."


def exercise_1_create_robots():
    r1 = Robot("R1-Ground")
    r2 = DroneRobot("R2-Drone", max_altitude=30)
    return r1, r2


def exercise_2_polymorphism_demo(robots):
    """Same method call, different behavior depending on the object's class."""
    return [robot.move() for robot in robots]


def exercise_3_total_count():
    return Robot.total_robots


if __name__ == "__main__":
    r1, r2 = exercise_1_create_robots()
    print("Exercise 1:", r1, "|", r2)
    print("Exercise 2 - polymorphism:", exercise_2_polymorphism_demo([r1, r2]))
    print("Exercise 3 - total robots created:", exercise_3_total_count())
