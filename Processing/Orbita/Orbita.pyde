import math as math
from data import *

earth_angle = 2*math.pi
moon_angle = 0

def setup():
	size(1800,1100)
	ellipseMode(CENTER)

def draw():
	background(0)

	screen_center_x = width/2
	screen_center_y = height/2

	sun['x'], sun['y'] = screen_center_x, screen_center_y

	fill(*YELLOW)
	circle(sun['x'], sun['y'], sun['diameter'])

	draw_planets(sun)

#-------------------------- MY FUNCTIONS ------------------------

def draw_planets(sun):
    
	last_planet = {'diameter': 0}
	
	for planet in planets:

		planet_diameter = planet['diameter']
		planet_distance = planet['distance'] + sun['diameter']/2 + last_planet['diameter']

		x_planet, y_planet = draw_orbit(sun['x'], sun['y'], planet_diameter, planet_distance, planet['angle'], planet['color'])
		planet['angle'] += 2*math.pi/planet['translate_time']/2

		if planet['name'] == 'earth':
			moon_distance = moon['distance'] + planet_diameter/2
			moon_diameter = moon['diameter']

			draw_orbit(sun['x'] + x_planet, sun['y'] + y_planet, moon_diameter, moon_distance, moon['angle'], moon['color'])
			moon['angle'] += 2*math.pi/moon['translate_time']/2

		last_planet = planet
    	

def draw_orbit(x, y, diameter, distance, angle, color):	
	radius = diameter/2

	pushMatrix()
	translate(x, y)

	fill(*color)
	x2 = (radius + distance) * math.cos(angle)
	y2 = (radius + distance) * math.sin(angle)
	circle(x2, y2, diameter)

	popMatrix()

	return x2, y2
