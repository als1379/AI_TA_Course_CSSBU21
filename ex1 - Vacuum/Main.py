from env import Env
from ai import Agent
from gui import cli_ui
from random import randint


if __name__ == "__main__":
    initial_Map = [
        [
            [-1,0,-1],
            [1,0,1]
        ],

        [
            [1,0,0,0],
            [0,0,1,0],
            [0,0,-1,0],
            [0,-1,1,0]
        ],
         ][randint(0,1)]

    sim = Env(initial_Map)
    agent1 = sim.add_agent(agent_class=Agent)
    gui = cli_ui()

    print("initial map")
    gui.display(sim.state)
    while not (sim.goal_test()):
        result=None
        while result != "success":
            action=agent1.act()
            print("attempting", action)
            result=sim.take_action(action, agent1)
            print(action, result)
        gui.display(sim.state)
        print("\n")

    print(
        "\n\nпобеда!!!",
        "\nyour cost (number of valid actions):", sim.perceive(agent1)["cost"],
        "\nyour score (number of cleared tiles):", sim.perceive(agent1)["score"]
    )
