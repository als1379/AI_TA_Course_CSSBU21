import random


class State:
    def __init__(self, map):
        self.map_array = map
        self.agent_list = []

    def get_agent_index(self, agent):
        agent_idxs = [idx for idx, ad in enumerate(self.agent_list) if ad["agent_obj"] == agent]
        if len(agent_idxs) == 0: print("agent not found"); return None
        else: return agent_idxs[0]

    def update(self, action, agent):
        ######### EDITABLE SECTION #########

        agent_idx = self.get_agent_index(agent)
        if agent_idx is None: return "invalid agent"
        if not self.validate_action(action): return "invalid action"

        self.update_score(action.lower(), agent_idx)
        self.update_map(action.lower(), agent_idx)

        return "success"

        ######### END OF EDITABLE SECTION #########

    def update_score(self, action, agent_idx):
        ######### EDITABLE SECTION #########

        self.agent_list[agent_idx]["agent_cost"] += 1

        i,j = self.agent_list[agent_idx]["agent_loc"]
        if action=="suck" and self.map_array[i][j]==1:
            self.agent_list[agent_idx]["agent_score"] += 1

        return "score and cost has been updated"

        ######### END OF EDITABLE SECTION #########

    def update_map(self, action, agent_idx):
        i,j = self.agent_list[agent_idx]["agent_loc"]

        ######### EDITABLE SECTION #########

        if action=="suck" and self.map_array[i][j]==1:
            self.map_array[i][j] = 0
            return "tile has been cleaned"
        if action=="suck": return "nothing to clean"

        delta_i, delta_j = {"up": (-1,0), "down": (+1,0), "right": (0,+1), "left": (0,-1)}[action]
        new_i, new_j=max(0,min(len(self.map_array)-1, i+delta_i)), max(0,min(len(self.map_array[0])-1, j+delta_j))

        with_agent_collision = [idx for idx, ad in enumerate(self.agent_list) if ad["agent_loc"]==(new_i,new_j)]
        if len(with_agent_collision)!=0 and with_agent_collision[0] != agent_idx: with_agent_collision=True

        if self.map_array[new_i][new_j]!=-1 and not with_agent_collision:
            self.agent_list[agent_idx]["agent_loc"]=(new_i,new_j)
            return "agent has moved to '%s'" %action

        return "nothing happened"

        ######### END OF EDITABLE SECTION #########

    def validate_action(self, action):
        if type(action) is not str or \
                action.lower() not in ["up", "down", "right", "left", "suck"]:
            print("the action '%s' is invalid" % action)
            return False
        return True


class Env:
    def __init__(self, map):
        self.state = State(map)

    def add_agent(self, agent_class):
        i,j = random.randint(0, len(self.state.map_array)-1), random.randint(0, len(self.state.map_array[0])-1)
        while self.state.map_array[i][j]==-1:
            i,j=random.randint(0, len(self.state.map_array)-1), random.randint(0, len(self.state.map_array[0])-1)

        self.state.agent_list.append({
            "agent_obj": agent_class(perceive_func=self.perceive),
            "agent_score": 0,
            "agent_cost": 0,
            "agent_loc": (i,j),
        })

        return self.state.agent_list[-1]["agent_obj"]

    def take_action(self, action, agent):
        return self.state.update(action, agent)

    def perceive(self, agent):
    
        ######### EDITABLE SECTION #########
        
        agent_data = self.state.agent_list[self.state.get_agent_index(agent)]
        return {
            "map": self.state.map_array,
            "agent_loc": self.state.map_array,
            "score": agent_data["agent_score"],
            "cost": agent_data["agent_cost"],
                }
                
        ######### END OF EDITABLE SECTION #########
        
    def goal_test(self):
        if any(1 in row for row in self.state.map_array):
            return False
        return True
