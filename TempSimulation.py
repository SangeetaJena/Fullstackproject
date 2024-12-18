import random    #importing random module to generate random numbers

# Simulating temperature readings
for i in range(1, 11):  # 10 temperature readings
    temperature = random.randint(20, 100)
    print(f"Reading {i}: Temperature = {temperature}°C")
    
    if temperature > 70:
        print("Danger! High temperature detected. Stopping monitoring.")
        break  # Stop monitoring when temperature exceeds safe limits


''' Make a game Guess the number
Generate random numbers between 1 and 10 and the u guess what that number can be
only three chances are allowed else print msg "You lost the game"
'''
