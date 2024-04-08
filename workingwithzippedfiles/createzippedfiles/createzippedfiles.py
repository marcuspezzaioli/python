import os
import zipfile

# Call each zip file zip1, zip2 etc.
zipped_file_base_name = "\\zip"

# Will store 5 files at a time in this example. 
# The size of each file should be taken into consideration when doing this.
files_to_include_in_one_zip_file = 5

# Gets the directories of the files to zip, and the directory we will store the zipped files in
files_to_zip_path = ".\\filestozip"
store_zipped_files_path = ".\\zippedfiles"

# Set name for first zipped files
suffix = "1"
file_extension = ".zip"
zipped_file_name = store_zipped_files_path + zipped_file_base_name + suffix + file_extension

# Create a counter to decide when enough files have been stored in the same zip
counter = 0

# Create a zip file object
zip_object = zipfile.ZipFile(zipped_file_name, 'w')

for file in os.listdir(files_to_zip_path): # Loops through everything in the filestozip directory.
        
        # arcname required to prevent several direcotry folders being stored in the actual zip
        # using the file name will mean that only the files are stored inside the zip, with no folder system used
        arcname = file

        if counter <= files_to_include_in_one_zip_file - 1:
                # Zip the file found
                zip_object.write(files_to_zip_path + "\\" +file, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)
                counter +=1
        else: 
                # reset the counter
                counter = 0

                # Close zip file object that has been created with first 5 files
                zip_object.close()

                # Get a new name for the next zip
                new_suffix = int(suffix) + 1
                suffix = str(new_suffix)
                zipped_file_name = store_zipped_files_path + zipped_file_base_name + suffix + file_extension

                # Update the zip_object
                zip_object = zipfile.ZipFile(zipped_file_name, 'w')
                zip_object.write(files_to_zip_path + "\\" +file, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)
                counter += 1



# Close the final zip object before exiting program to ensure all data is saved correctly
zip_object.close()