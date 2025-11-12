def calculate_volume_of_sphere(radius):
    """Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    import math
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

x = calculate_volume_of_sphere(30)
print(x)

y = calculate_volume_of_sphere(40)
print(y)