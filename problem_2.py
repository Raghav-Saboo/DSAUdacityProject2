import os


def find_files(suffix, path, ans):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

  Returns:
     a list of paths
  """
  for curr_file in os.listdir(path):
    abs_file_path = os.path.join(path, curr_file)
    if os.path.isfile(abs_file_path) and curr_file.endswith(suffix):
      ans.append(abs_file_path)
    elif os.path.isdir(abs_file_path):
      find_files(suffix, abs_file_path, ans)
  return None


ans = []
find_files(suffix='.h', path=os.curdir, ans=ans)
print(ans)
