import numpy as np
import matplotlib.pyplot as plt
from pid_controller import PID
from torque_model import compute_inertia, compute_torque

# Params
wheel_mass = 0.7  # kg
wheel_radius = 0.2  # meters 
sat_mass = 1.7  # kg (simplified)
sat_radius = 0.15  # meters 

# Moment of inertia
I_wheel = compute_inertia(wheel_mass, wheel_radius)
I_sat = compute_inertia(sat_mass, sat_radius)

# PID setup
pid = PID(kp=1.7, ki=0.2, kd=5.0)
target_angle = np.pi / 2  #degree to radian 

# Sim loop setup
dt = 0.05  # seconds
time = np.arange(0, 10, dt)
angle = 0
angular_velocity = 0
angles = []

for t in time:
    #desired angular accelaration
    control_output = pid.compute(target_angle, angle, dt)

    # Convert to torque (wheel spins -> sat rotates opposite)
    torque = compute_torque(I_wheel, control_output)
    angular_acceleration = torque / I_sat

    # Update satellite orientation
    angular_velocity += angular_acceleration * dt
    angle += angular_velocity * dt

    angles.append(angle)

# Plot
plt.plot(time, angles)
plt.axhline(target_angle, color='r', linestyle='--', label='Target')
plt.title("Satellite Orientation Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.grid(True)
plt.show()
