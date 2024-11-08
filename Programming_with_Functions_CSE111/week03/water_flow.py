def water_column_height(tower_height, tank_height):
    """Calculate the height of a column of water from a tower height and a tank wall height.

    Parameters
        tower_height (float): The height of the tower.
        tank_height (float): The height of the walls of the tank that is on top of the tower.
    Return: float: The height of the water column.
    """
    # Calculate the water column height using the formula
    water_height = tower_height + (3 * tank_height) / 4
    return water_height


def pressure_gain_from_water_height(height):
    """Calculate the pressure caused by Earth's gravity pulling on the 
    water stored in an elevated tank.

    Parameters
        height (float): The height of the water column in meters.
    Return: float: The pressure in kilopascals.
    """
    # Calculate the pressure using the formula P = ρgh / 1000
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """the water pressure lost due to friction within a pipe.

    Parameters
        pipe_diameter (float): The diameter of the pipe in meters.
        pipe_length (float): The length of the pipe in meters.
        friction_factor (float): The pipe's friction factor.
        fluid_velocity (float): The velocity of the water flowing 
        through the pipe in meters/second.
    Return the suffix, if any, that appears in both string1 and
    """
    # Calculate the pressure loss using the formula P = -f * L * ρ * v^2 / (2000 * d)
    pressure_loss = -friction_factor * pipe_length * 998.2 * fluid_velocity**2 / (2000 * pipe_diameter)
    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_of_water = 998.2  # in kg/m^3
    pressure_loss = -0.04 * density_of_water * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss


def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_of_water = 998.2  # in kg/m^3
    dynamic_viscosity_of_water = 0.0010016  # in Pa·s
    reynolds_number = (density_of_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_of_water
    return reynolds_number


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_of_water = 998.2  # in kg/m^3
    constant_k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -(constant_k * density_of_water * fluid_velocity ** 2) / 2000
    return pressure_loss



PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    
    

if __name__ == "__main__":
    main()




         



