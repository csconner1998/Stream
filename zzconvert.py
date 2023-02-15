import os
import sys

# Get the source and destination directories
source_directory = "./zoomImages"
destination_directory = "./backup"

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
  # Check if the file is a JPG image
  if filename.endswith(".jpg"):
    # Construct the source and destination paths
    source_path = os.path.join(source_directory, filename)
    destination_path = os.path.join(destination_directory, filename)
    # Move the file from the source to the destination
    os.rename(source_path, destination_path)
