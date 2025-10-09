#this is a tool to calculate the trajectory of a football/soccer ball in motion with the application of air resistance i made a couple years ago, the constants are available to change if needed, and the angle/speed further down in the code

import math
import matplotlib.pyplot as plt

def calculate_trajectory(initial_speed, launch_angle):
    ball_mass = 0.41  
    gravity = 9.80665  
    air_density = 1.225  
    drag_coefficient = 0.47  
    ball_radius = (0.68 / (2 * math.pi) + 0.70 / (2 * math.pi)) / 2  
    cross_sectional_area = math.pi * ball_radius ** 2  

    launch_angle_rad = math.radians(launch_angle)

    initial_height = 0  
    initial_position = (0, initial_height)  
    initial_velocity = (initial_speed * math.cos(launch_angle_rad), initial_speed * math.sin(launch_angle_rad))  

    dt = 0.001
    simulation_time = 10 

    time = [0]
    position = [initial_position]

    while position[-1][1] >= 0 and time[-1] <= simulation_time:
        velocity = math.sqrt(initial_velocity[0] ** 2 + initial_velocity[1] ** 2)
        drag_force = 0.5 * air_density * velocity ** 2 * drag_coefficient * cross_sectional_area

        acceleration_x = -drag_force / ball_mass * initial_velocity[0] / velocity
        acceleration_y = -gravity - drag_force / ball_mass * initial_velocity[1] / velocity

        new_velocity_x = initial_velocity[0] + acceleration_x * dt
        new_velocity_y = initial_velocity[1] + acceleration_y * dt

        new_position_x = initial_position[0] + initial_velocity[0] * dt
        new_position_y = initial_position[1] + initial_velocity[1] * dt

        time.append(time[-1] + dt)
        position.append((new_position_x, new_position_y))

        initial_velocity = (new_velocity_x, new_velocity_y)
        initial_position = (new_position_x, new_position_y)

    time_of_flight = time[-1]

    range_of_ball = position[-1][0]

    return time_of_flight, range_of_ball, time, position

initial_speeds = [5, 10, 15, 20, 25, 30] 
launch_angle = 25 

time_of_flights = []
ranges = []

for speed in initial_speeds:
    time_of_flight, range_of_ball, time, position = calculate_trajectory(speed, launch_angle)
    time_of_flights.append(time_of_flight)
    ranges.append(range_of_ball)

    plt.plot([pos[0] for pos in position], [pos[1] for pos in position], label=f"Initial Speed: {speed} m/s")
    plt.text(position[-1][0], position[-1][1], f"Time of Flight: {time_of_flight:.2f} s", ha='right', va='bottom')

    range_of_ball *= 1.05
    plt.plot([0, range_of_ball], [0, 0], 'k--')

plt.xlabel("Sx Displacement (m)")
plt.ylabel("Sy Vertical Displacement (m)")
plt.title("Sy Displacement vs Sx Displacement:")
plt.legend()
plt.grid(True)

plt.show()

for i in range(len(initial_speeds)):
    print(f"Initial Speed: {initial_speeds[i]} m/s")
    print(f"Time of Flight: {time_of_flights[i]} s")
    print(f"Range: {ranges[i]} m")
    print()
