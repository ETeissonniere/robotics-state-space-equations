# Spring mass system
#
# The state is represented as:
# - x_1: position along the x axis
# - x_2: velocity along the x axis
#
# As per newton's second law of motion, F = m * a.
# Couple forces are applied to the system:
# - Spring force: F_spring = -k * x_1
# - Damping force: F_damping = -c * x_2
# - External force: F_external = u
#
# So:
# m * x_2' = F_spring + F_damping + F_external
# m * x_2' = -k * x_1 - c * x_2 + u
# x_2' = (-k * x_1 - c * x_2 + u) / m
#
# Thus, this gives us:
# - x_1' = x_2
# - x_2' = (-k * x_1 - c * x_2 + u) / m
#
# Converting to state space, we get: 
# x = [x_1 x_2]
# x' = [x_1'] = A * x + B * u = [0       1] * x + [0  ] * u
#      [x_2']                   [-k/m -c/m]       [1/m]
#
# Since we only care about position, we can set y as:
# y = [x_1] = C * x + D * u = [1 0] * x + [0] * u

