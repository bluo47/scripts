import zipfile
import os

# Specify the name of the compressed file and the files to include
zip_filename = 'WHO-COVID-19-global-data.csv.zip'
files_to_compress = ['WHO-COVID-19-global-data.csv']

# Create a new ZipFile object
with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
    # Add each file to the archive
    for file in files_to_compress:
        myzip.write(file)

print('Compression completed')
file_size_bytes = os.path.getsize(zip_filename)
file_size_mb = round((file_size_bytes / (1024 * 1024)),2)

print(f'The size of {zip_filename} is {file_size_mb} MB')
