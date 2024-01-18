# bag-ply-converter

The team works with 3D camera data.
The team needs to occasionally convert 3D data from BAG format to PLY.
Thus a command line tool is needed. The tool should take a path to a BAG file as input, make a conversion, and save it as a PLY file.
The tool can be occasionally updated, so a GitHub repository is needed to keep track of changes. Also, the team wants to be able to see how changes affect the code. Thus a pipeline is needed to lint the code and to run tests.

Requirements:

- [ ] The tool shall be written in Python language.
- [ ] The tool shall be an executable.
- [ ] The tool shall run on Linux OS.
- [ ] The tool shall take the path to a bag file as input.
- [ ] The tool shall save a file in PLY format as output.
- [ ] The tool shall utilize the save_to_ply() function from the [pyrealsense2](https://pypi.org/project/pyrealsense2/) library ([reference](https://github.com/IntelRealSense/librealsense/blob/master/wrappers/python/examples/export_ply_example.py)).
- [ ] The tool shall be hosted on a public GitHub repository.
- [ ] The repository shall run a workflow to lint the code upon a push to the main branch.
- [ ] The repository shall run a workflow to unit test the code upon push to the main branch.

A [bag file](test.bag) in the repository can be used together with the [test cases](converter_tests.py).
