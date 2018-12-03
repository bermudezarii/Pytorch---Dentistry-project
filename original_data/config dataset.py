#libs 
import os
import shutil

#directories used 
rootdir = '/home/miuser/Downloads/Ariana/datasets/' #default 
copydir_normal = '/home/miuser/Downloads/Ariana/datasets/All/' #where x-rays are going to be 
copydir_seg = '/home/miuser/Downloads/Ariana/datasets/All_segmented/' #where all segmented teeth are going to be 
copydir_mouth = '/home/miuser/Downloads/Ariana/datasets/All_mouth/' # where all mouth segmentation goes 


#this for explores the directories, subdirectories and files from given rootdir 
for subdir, dirs, files in os.walk(rootdir):
    #each file 
    for file in files:
        #split the string, you could print it (subdir) and notice it's the path 
        # from file without the name of the file 
        split_str = subdir.split("/")
        # manual counting to know which file is which
        
        #normal xrays 
        if(len(subdir) == 58 or len(subdir) == 59):
            #source address
            src_file = os.path.join(subdir, file)
            #copy the file to the new source 
            shutil.copy(src_file, copydir_normal) 
            #creates the new name of the file 
            new_name = copydir_normal  + split_str[-2]+"_"+file 
            #gets the new route of the file 
            dst_file = os.path.join(copydir_normal, file) 
            #rename the file 
            os.rename(dst_file, new_name) 
        
        #segmented teeth 
        elif(len(subdir) == 75 or len(subdir) == 76):
            src_file = os.path.join(subdir, file)
            shutil.copy(src_file, copydir_seg) 
            new_name = copydir_seg  + split_str[-3]+"_"+file 
            dst_file = os.path.join(copydir_seg, file) 
            os.rename(dst_file, new_name) 
            
        #segmented mouths
        elif(len(subdir) == 81 or len(subdir) == 82):
            src_file = os.path.join(subdir, file)
            shutil.copy(src_file, copydir_mouth) 
            new_name = copydir_mouth  + split_str[-4]+"_"+file 
            dst_file = os.path.join(copydir_mouth, file) 
            os.rename(dst_file, new_name) 
        
#done by Ari (: