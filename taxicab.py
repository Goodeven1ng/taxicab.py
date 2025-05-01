# Mutaz Al-Shara
# Instructor Rita Ghantous
# Engr_103_401_S025
# 04-30-2025
class Taxicab:
    """
    A class representing a Taxicab with x and y coordinates and an odometer.
    
    Attributes:
        _x_coord (int): The current x-coordinate of the Taxicab.
        _y_coord (int): The current y-coordinate of the Taxicab.
        _odometer (int): The total distance traveled by the Taxicab.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initialize the Taxicab with x and y coordinates and set the odometer to zero.
        
        Parameters:
            x_coord (int): Initial x-coordinate.
            y_coord (int): Initial y-coordinate.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Return the current x-coordinate of the Taxicab.
        
        Returns:
            int: The x-coordinate.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Return the current y-coordinate of the Taxicab.
        
        Returns:
            int: The y-coordinate.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Return the current odometer reading of the Taxicab.
        
        Returns:
            int: The odometer reading.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Move the Taxicab horizontally by the specified distance and update the odometer.
        
        Parameters:
            distance (int): Distance to move along the x-axis (positive for right, negative for left).
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Move the Taxicab vertically by the specified distance and update the odometer.
        
        Parameters:
            distance (int): Distance to move along the y-axis (positive for up, negative for down).
        """
        self._y_coord += distance
        self._odometer += abs(distance)
