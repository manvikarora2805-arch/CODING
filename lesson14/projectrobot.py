class Robot:
    # The Constructor: Initializes the robot's attributes
    def __init__(self, name, model, purpose, battery_level=100):
        self.name = name
        self.model = model
        self.purpose = purpose
        self.battery_level = battery_level

    # A Method to make the robot introduce itself
    def introduce(self):
        print(f"🤖 Hello! My name is {self.name}.")
        print(f"📟 Model: {self.model}")
        print(f"🚀 My main purpose is: {self.purpose}.")
        print(f"🔋 Current Battery: {self.battery_level}%")
        print("-" * 40)

    # A Method to show the robot performing an action
    def perform_task(self, task_name):
        if self.battery_level > 10:
            print(f"⚡ {self.name} is now performing the task: '{task_name}'...")
            self.battery_level -= 15  # Using the task drains some battery
            print(f"🔋 Task complete! Battery is now at {self.battery_level}%.")
        else:
            print(f"⚠️ Low battery! {self.name} needs to charge before working.")
        print("-" * 40)


# --- Creating Objects (Instances of the Robot Class) ---

# Creating the first robot instance
robot_one = Robot(name="Sparky", model="Astro-Bot v1.0", purpose="Explore the galaxy")

# Creating a second robot instance
robot_two = Robot(name="Bolt", model="Helper-Bot v2.4", purpose="Assist with coding assignments")


# --- Executing the Program ---

# Introducing and testing Sparky
print("=== ROBOT 1 ===")
robot_one.introduce()
robot_one.perform_task("Scanning Mars for water")

# Introducing and testing Bolt
print("=== ROBOT 2 ===")
robot_two.introduce()
robot_two.perform_task("Reviewing Python code templates")