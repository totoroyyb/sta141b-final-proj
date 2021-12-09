import pathlib

class PathResolver():
    '''
    You can access the static variable to get all path for different folders.
    '''

    code_dir = pathlib.Path(__file__).parent.resolve()
    parent_dir = code_dir.parent.resolve()

    data_dir = parent_dir.joinpath("data")
    notebook_dir = parent_dir.joinpath("notebooks")
    