import os
import shutil

def recursive_copy(source_dir, destination_dir):
  """
  Recursively copies all contents from a source directory to a destination directory.

  Args:
      source_dir (str): The path to the source directory.
      destination_dir (str): The path to the destination directory.
  """
  try:
      # Remove contents in destination directory before copying
      if os.path.exists(destination_dir):
          shutil.rmtree(destination_dir)
      # Create the destination directory if it doesn't exist
      if not os.path.exists(destination_dir):
          os.makedirs(destination_dir)

      for item in os.listdir(source_dir):
          source_path = os.path.join(source_dir, item)
          destination_path = os.path.join(destination_dir, item)

          if os.path.isdir(source_path):
              recursive_copy(source_path, destination_path)
          else:
              print(f"Copying file: {source_path} to {destination_path}")
              shutil.copy(source_path, destination_path)

      print(f"Successfully copied contents from '{source_dir}' to '{destination_dir}'")
  except shutil.Error as e:
      print(f"Error copying directory: {e}")
  except OSError as e:
      print(f"OS Error: {e}")