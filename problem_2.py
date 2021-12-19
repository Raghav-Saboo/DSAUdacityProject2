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


# Test Case 1
ans = []
find_files(suffix='.h', path=os.curdir, ans=ans)
print(
    'Pass' if ans == ['./testdir/subdir3/subsubdir1/b.h',
                      './testdir/subdir5/a.h',
                      './testdir/t1.h', './testdir/subdir1/a.h'] else 'Fail')

# Test Case 2
ans = []
find_files(suffix='.c', path=os.curdir, ans=ans)
print(
    'Pass' if ans == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c',
                      './testdir/subdir5/a.c',
                      './testdir/subdir1/a.c'] else 'Fail')

# Test Case 3
ans = []
find_files(suffix='.java', path=os.curdir, ans=ans)
print('Pass' if ans == [] else 'Fail')
