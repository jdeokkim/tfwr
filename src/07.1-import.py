#
# Copyright (c) 2025 Jaedeok Kim <jdeokkim@protonmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

# ============================================================================>

import modules.utils as utils

# ============================================================================>

# The number of columns which should be reserved to grow pumpkins.
RESERVED_COLUMN_COUNT = 4

# The current size of the farm.
WORLD_SIZE = get_world_size()

# ============================================================================>

def init():
	clear()
	
	change_hat(Hats.Traffic_Cone_Stack)

	# NOTE: Wait until we're ready to harvest our first plant
	while not can_harvest():
		pet_the_piggy()


# ============================================================================>

def plant_on(x, y):
	# NOTE: Make sure trees have enough space between them
	x_mod_3, y_mod_2 = (x % 3), (y % 2)

	if x < RESERVED_COLUMN_COUNT:
		utils.plant_pumpkin()
	else:
		if x_mod_3 == 0:
			utils.plant_grass()
		elif x_mod_3 == 1:
			if y_mod_2 == 0:
				utils.plant_sunflower()
			else:
				utils.plant_tree()
		else:
			utils.plant_carrot()

	use_item(Items.Fertilizer)


# ============================================================================>
		
if __name__ == "__main__":
	init()
	
	i = 0
	
	while True:
		quick_print("Iteration #", i, "->", get_tick_count())
		
		for y in range(WORLD_SIZE):
			for x in range(WORLD_SIZE):	
				if can_harvest():
					harvest()
	
					plant_on(x, y)
					
				utils.water()
				
				move(East)
			
			move(North)
			
		i += 1

# ============================================================================>
