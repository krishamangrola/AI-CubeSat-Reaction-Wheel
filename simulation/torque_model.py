import numpy as np

def compute_inertia(mass, radius):
    return 0.5 * mass * (radius ** 2)

def compute_torque(inertia, angular_acceleration):
    return inertia * angular_acceleration

# Example usage
if __name__ == "__main__":
    mass = 0.5  # kg
    radius = 0.1  # m
    angular_acc = 5  # rad/s^2

    I = compute_inertia(mass, radius)
    torque = compute_torque(I, angular_acc)
    
    print(f"Moment of Inertia: {I:.4f} kg·m²")
    print(f"Torque: {torque:.4f} N·m")
