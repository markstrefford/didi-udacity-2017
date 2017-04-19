#  http://graphicdesign.stackexchange.com/questions/1481/in-gimp-how-to-save-the-different-layers-of-a-design-in-separate-files-images
#  http://stackoverflow.com/questions/5794640/how-to-convert-xcf-to-png-using-gimp-from-the-command-line

# for layer in image.layers:
#         filename = join(directory, name_pattern % layer.name)
#         raw_filename = name_pattern % layer.name
#         pdb.gimp_file_save(image, layer, filename, raw_filename)



# in python 2.7
from gimpfu import *
import glob
import os


#--------------------------------------------------------------------------------------
gimp_dir  = '/root/share/project/didi/data/didi/didi-2/Out/1/15/processed/mayavi_top-fg-xcf'
mask_dir  = '/root/share/project/didi/data/didi/didi-2/Out/1/15/processed/mayavi_top-fg-mask'

if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)

for file in sorted(glob.glob(gimp_dir + '/*.xcf')):
    name = os.path.basename(file).replace('.xcf','')  #'%06d'%t

    print ('running file = %s'%name)
    gimp_file = gimp_dir   + '/' + name + '.xcf'
    mask_file = mask_dir   + '/' + name + '.png'

    image = pdb.gimp_xcf_load(0, gimp_file, gimp_file)
    layer = image.layers[0]

    pdb.gimp_file_save(image, layer, mask_file, mask_file)


'''
gimp -idf --batch-interpreter python-fu-eval -b 'execfile("/root/share/project/didi/build/baseline-04/didi_data/gimp_scripts/split_xcf.py"); pdb.gimp_quit(1)'
  
  
'''
