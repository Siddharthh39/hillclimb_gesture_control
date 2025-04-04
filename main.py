import os

def show_menu():
    print("Choose Game Mode:")
    print("1. Hill Climb Racing")
    print("2. hollowKnight")
    choice = input("Enter your choice (1/2): ").strip()
    return choice

if __name__ == "__main__":
    choice = show_menu()

    if choice == '1':
        import hillclimb_mode
        hillclimb_mode.run()
    
    elif choice == '2':
        import hollowKnigh
        hollowKnigh.run()
    
    else:
        print("Invalid choice.")
