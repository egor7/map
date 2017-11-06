#!/usr/bin/python
import os, glob

with open('world.txt') as f:
	world_txt_lines  = f.readlines()
world_txt_lines = [x.strip() for x in world_txt_lines] 


tgt = 'montage '
for i, r in enumerate(world_txt_lines):
	if i == 0:
		r_prev = r
		continue

	row = 'montage '
	for j in range(1,len(r)):
 		t1 = str(r_prev[j])
 		t2 = str(r_prev[j-1])
 		t3 = str(r[j-1])
 		t4 = str(r[j])
		row += t1 + t2 + t3 + t4 + '.png '

	tgt_row = 'r_' + str(i) + '.png'

	row += '-mode Concatenate -tile x1 ' + tgt_row
	tgt += tgt_row + ' '

	print row
	os.system(row)

	r_prev = r

tgt += '-mode Concatenate -tile 1x ' + 'world.png'
print tgt
os.system(tgt)

for f in glob.glob('r_*.png'):
	os.remove(f)
