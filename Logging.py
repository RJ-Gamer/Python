""" Logging Have 5 Built in Levels:
    DEBUG, INFO, WARNING, ERROR, CRITICAL """

import logging
import math
#print dir(logging)
"""


# Test the logger
logger.info("This is Logger INFO")
print logger.level

#Test messages
logger.debug("This is a harmless DEBUG message")
logger.info("This is a USEFUL info message")
logger.warning("I'm Sorry..! But That action can't be taken")
logger.error("Did you just try to divide by Zero")
logger.critical("The Entire system is down")
"""

LOG_FORMAT =  "%(levelname)s -- %(asctime)s -- %(message)s"
logging.basicConfig(filename = "myconfig.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

def quadratic_equation(a,b,c):
    """"Return the solution to the ax^2 + bx + c = 0"""
    logger.info("quadratic_equation({0}, {1}, {2})".format(a,b,c))

    # Compute the Discriminant
    logger.debug("#Compute The Discriminant")
    disc = b**2 - 4*a*c

    #Compute the Two Roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / 2*a
    root2 = (-b + math.sqrt(disc)) / 2*a

    #Return the two Roots
    logger.debug("# Return the Roots")
    return(root1, root2)

roots = quadratic_equation(1,0,-4)
print(roots)
