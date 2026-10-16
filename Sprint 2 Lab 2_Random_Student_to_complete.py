import random
import time
from easytello import tello

# Initialize the drone
drone = tello.Tello()

# Step 1: Record Attitude and height
def record_att_data():
    # Get attitude and height data from the drone
    attitude = drone.get()
    height =
    # Append data to the file
    with open('attitude_height_data.txt', 'a') as file:
        file.write(f'Attitude: {attitude}, Height: {height}\n')
    time.sleep(1)

# Step 2: Implement Randomized Flight
def random_flight():
    #have this loop 3 times
    for i in range():
        # Generate random X, Y, Z coordinates
        x = random.randint(-20, 20)  # Adjust the range as needed
        y =
        z =   # Drone flies at a height between 20cm and 50cm
        # Apply random coordinates to drone movement commands
        drone.go(x, y, z, speed=35)  # Adjust speed as needed
        #drone.forward(random.randint(20, 50))  # e.g Move forward by a random distance
        # Implement more random commands like 'up()', 'down()', 'cw()', etc., as desired
        record_att_data()
        # Sleep for a random duration before the next command
        sleep_duration = random.uniform(1, 3)  # Adjust the range as needed
        time.sleep(sleep_duration)


#this is where our code STARTS
drone.takeoff()
random_flight()

#need to add landing code!

