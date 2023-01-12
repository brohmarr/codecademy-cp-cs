# Project: Getting Ready for Physics Class
# by: @Brohmarr

# You are a physics teacher preparing for the upcoming semester. You
#     want to provide your students with some functions that will help
#     them calculate some fundamental physical properties.


# Initial data.
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Converts a temperature in Fahrenheit to Celsius.
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5 / 9)

  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Converts a temperature in Celsius to Fahrenheit.
def c_to_f(c_temp):
  f_temp = (c_temp * (9 / 5)) + 32

  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Calculates the force (mass * acceleration).
def get_force(mass, acceleration):
  return (mass * acceleration)

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Returns the energy (((mass * c) ** 2) / 2, where c is usually set to
#     the speed of light).
def get_energy(mass, c = 3 * (10 ** 8)):
  return (((mass * c) ** 2) / 2)

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Returns the work (force * distance).
def get_work(mass, acceleration, distance):
  return ((get_force(mass, acceleration)) * distance)

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " +
      str(train_distance) + " meters.")
