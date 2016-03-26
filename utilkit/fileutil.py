"""
File/directory helper functions
Copying of file trees, creating directories, reading files and more
"""
import os
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


def ensure_dir_exists(f):
    """
    Ensure the existence of the parent directory of f
    """
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


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
