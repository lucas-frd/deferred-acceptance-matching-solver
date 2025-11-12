from src.solver import DeferredAcceptanceSolver

def main():
    num_proposers = int(input("Enter the number of proposers: "))
    proposer_preferences = []
    proposed_preferences = []

    for i in range(1, num_proposers + 1):
        while True:
            preferences = input(f"Enter preferences for proposer {i} (space-separated): ")
            pref_list = [int(x) - 1 for x in preferences.split()]
            if len(pref_list) != num_proposers:
                print(f"Error: You must enter exactly {num_proposers} preferences.")
            elif set(pref_list) != set(range(num_proposers)):
                print(f"Error: Preferences must include each number from 1 to {num_proposers} exactly once.")
            else:
                break
        proposer_preferences.append(pref_list)

    for i in range(1, num_proposers + 1):
        while True:
            preferences = input(f"Enter preferences for proposed {i} (space-separated): ")
            pref_list = [int(x) - 1 for x in preferences.split()]
            if len(pref_list) != num_proposers:
                print(f"Error: You must enter exactly {num_proposers} preferences.")
            elif set(pref_list) != set(range(num_proposers)):
                print(f"Error: Preferences must include each number from 1 to {num_proposers} exactly once.")
            else:
                break
        proposed_preferences.append(pref_list)
    
    solver = DeferredAcceptanceSolver(proposer_preferences, proposed_preferences)
    matches = solver.solve()

    for i, match in enumerate(matches):
        print(f"Proposer {i + 1} is matched with Proposed {match + 1}")



if __name__ == "__main__":
    main()