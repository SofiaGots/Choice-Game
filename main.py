from data import GAME_STATE

current = "start"

while current is not None:
    state = GAME_STATE[current]

    print()
    print(state["location"])
    print(state["question"])

    for i in range(len(state['choices'])):  
        print(f"{i+1}. {state['choices'][i][0]}")

    choice = int(input("Your choice: "))
    current = state["choices"][choice - 1][1]
