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

WATER_LEVEL_THRESHOLD = 0.5

# ============================================================================>

def plant_bush():
	plant(Entities.Bush)


def plant_carrot():
	if get_ground_type() == Grounds.Grassland:
		till()
	
	plant(Entities.Carrot)


def plant_grass():
	plant(Entities.Grass)


def plant_pumpkin():
	if get_ground_type() == Grounds.Grassland:
		till()

	plant(Entities.Pumpkin)


def plant_sunflower():
	if get_ground_type() == Grounds.Grassland:
		till()

	plant(Entities.Sunflower)


def plant_tree():
	plant(Entities.Tree)


# ============================================================================>

def fertilize():
	if (num_items(Items.Fertilizer) < 1):
		return

	use_item(Items.Fertilizer)


def water():
	if (get_water() >= WATER_LEVEL_THRESHOLD) or (num_items(Items.Water) < 1):
		return

	use_item(Items.Water)


# ============================================================================>