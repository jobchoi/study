import sys

# [1. 신호등]
# [2. 가위바위보 게임]
# [3. 도형 그리기]

class Select:
    def __init__(self):
        self.choices = {
            '1': self.traffic_light,
            '2': self.rock_paper_scissors,
            '3': self.draw_shape
        }

    def traffic_light(self):
        print("Traffic Light selected.")
        # Implement traffic light logic here

    def rock_paper_scissors(self):
        print("Rock-Paper-Scissors selected.")
        # Implement rock-paper-scissors logic here

    def draw_shape(self):
        print("Draw Shape selected.")
        # Implement shape drawing logic here

    def run(self):
        while True:
            print("\nSelect a program to run:")
            print("1. Traffic Light")
            print("2. Rock-Paper-Scissors")
            print("3. Draw Shape")
            print("q. Quit")

            choice = input("Enter your choice: ").strip()
            if choice == 'q':
                print("Exiting the program.")
                sys.exit()
            elif choice in self.choices:
                self.choices[choice]()
            else:
                print("Invalid choice. Please try again.")

Select.draw_shape():
    

if __name__ == "__main__":
    app = Select()
    app.run()