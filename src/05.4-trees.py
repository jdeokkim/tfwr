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

clear()

# ============================================================================>

i = 0

# ============================================================================>

while True:
	quick_print("Iteration #", i)
	
	n = get_world_size()
	
	for y in range(n):
		for x in range(n):
			if not can_harvest():
				do_a_flip()
			
			harvest()

			# NOTE: We need to harvest 3 types of plants at once
			m = (x % 3)
				
			if m == 0:
				plant(Entities.Grass)
			elif m == 1:
				# NOTE: Make sure trees have enough space between them
				if (y % 2) == 0:
					plant(Entities.Bush)
				else:
					plant(Entities.Tree)
			else:
				# NOTE: This cell should always be soil
				if get_ground_type() == Grounds.Grassland:
					till()
				
				plant(Entities.Carrot)
				
			if get_water() < 0.5:
				quick_print("get_water(): ", get_water())

				use_item(Items.Water)
			
			move(East)
		
		move(North)
		
	i += 1


# ============================================================================>
