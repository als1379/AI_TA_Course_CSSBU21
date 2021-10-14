class cli_ui:
    def __init__(self):
        pass

    def display(self, env):
        replace_dict = {-1: "///", 0: "   ", 1: " d "}

        final_list=[["___" for _ in range(len(env.map_array[0])+2)]]
        for row in env.map_array:
            final_list.append([" | "]+list(replace_dict[tile] for tile in row)+[" | "])
        final_list.append(["___" for _ in range(len(env.map_array[0])+2)])
        final_list[0][0]=final_list[-1][0]=" __"
        final_list[0][-1]=final_list[-1][-1]="__ "

        for ad in env.agent_list:
            i,j = ad["agent_loc"]
            if final_list[i+1][j+1]==" d ": final_list[i+1][j+1] = "dX "
            else: final_list[i+1][j+1] = " X "

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in final_list]))