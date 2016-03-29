"""
File/directory helper functions
Copying of file trees, creating directories, reading files and more
"""
import os
import datetime
import shutil


def copytree(src, dst, symlinks = False, ignore = None):
    """
    Copy a tree of files and dirs and merge into existing dir if needed
    Source: http://stackoverflow.com/a/22331852
    """
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)
    lst = os.listdir(src)
    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]
    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except:
                pass # lchmod not available
        elif os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def archive_if_exists(filename):
    """
    Move `filename` out of the way, archiving it by appending the current datetime
    Can be a file or a directory
    """
    if os.path.exists(filename):
        current_time = datetime.datetime.now()
        dt_format = '%Y-%m-%dT%H:%M:%S%z'
        timestamp = current_time.strftime(dt_format)
        dst = filename + '_' + timestamp
        shutil.move(filename, dst)


def ensure_dir_exists(f, fullpath=False):
    """
    Ensure the existence of the (parent) directory of f
    """
    if fullpath == False:
        # Get parent directory
        d = os.path.dirname(f)
    else:
        # Create the full path
        d = f
    if not os.path.exists(d):
        os.makedirs(d)


def list_files(dirname):
    """
    List all files in directory `dirname`
    """
    f = []
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        f.extend(filenames)
        break
    return f


def get_file_contents(filename):
    """
    Read file contents from file `filename`
    """
    data = None
    try:
        with open(filename) as pf:
            data = pf.read()
    except IOError:
        # File not found, return None
        pass
    return data
