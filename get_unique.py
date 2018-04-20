import os

inp_dir = './input'
os.system('rm unique.txt')


unique_list = []

with open('unique.txt','a') as op_file:
	for _,_,files in os.walk(inp_dir):
		print('reading files')
		for file in files:
			filename = os.path.join(inp_dir,file)
			f = open(filename,'r').read()
			f_list = f.split()
			print(f'{len(f_list)} words found in {filename}')
			for word in f_list:
				if word not in unique_list:
					unique_list.append(word)
					op_file.write(word + '\n')
				else:
					print(f'repeating word = {word}')