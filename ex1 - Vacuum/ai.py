class Agent:
    def __init__(self, perceive_func=None):
        self.perceive_func = perceive_func

        ######### EDITABLE SECTION #########

        ######### END OF EDITABLE SECTION #########

    def act(self):
        sensor_data = self.perceive_func(self)

        ######### EDITABLE SECTION #########

        import random
        action = random.choice(["right", "left", "up", "down", "suck"])

        ######### END OF EDITABLE SECTION #########

        return action
