# http://stackoverflow.com/questions/42630994/gimp-python-fu-how-to-create-and-save-multilayer-xcf-from-1-jpg-and-1-png
# http://stackoverflow.com/questions/12662676/writing-a-gimp-python-script


# in python 2.7
from gimpfu import *
import glob
import os



#--------------------------------------------------------------------------------------


image_dir  = '/root/share/project/didi/data/didi/didi-2/Out/1/15/processed/mayavi_top-fg'
gimp_dir   = '/root/share/project/didi/data/didi/didi-2/Out/1/15/processed/mayavi_top-fg-xcf'
mask_file  = '/root/share/project/didi/data/didi/didi-2/Out/processed/mask.png'
 

 
if not os.path.exists(gimp_dir):
    os.makedirs(gimp_dir)




for file in sorted(glob.glob(image_dir +'/*.png')):
    name = os.path.basename(file).replace('.png','')  #'%06d'%t


    print ('running file = %s'%name)
    img_file  = image_dir  + '/' + name + '.png'
    gimp_file = gimp_dir   + '/' + name + '.xcf'

    image=pdb.gimp_file_load(img_file,img_file)
    layer=pdb.gimp_file_load_layer(image,mask_file)
    layer.opacity = 50. #1-100

    image.add_layer(layer,0)
    pdb.gimp_xcf_save(0,image,layer,gimp_file,gimp_file)


#https://www.gimp.org/tutorials/Basic_Batch/


'''
gimp -idf --batch-interpreter python-fu-eval -b 'execfile("/root/share/project/didi/build/baseline-04/didi_data/gimp_scripts/merge_xcf.py"); pdb.gimp_quit(1)'
  
  
  
'''
