from setuptools import setup, find_packages
import ast
import os

# Extract version from blenderproc/version.py
here = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(here, "blenderproc", "version.py")) as fp:
    exec(fp.read(), version)

with open(os.path.join(here, "README.md")) as fp:
    long_description = fp.read()

# Blender version whose pip "bpy" module BlenderProc supports, keep in sync with InstallUtility.py
bpy_version = "5.2.3"


def read_default_pip_packages():
    """ Reads DefaultConfig.default_pip_packages, the python packages BlenderProc needs next to bpy. """
    with open(os.path.join(here, "blenderproc", "python", "utility", "DefaultConfig.py")) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(target, "id", None) == "default_pip_packages"
                                                for target in node.targets):
            return ast.literal_eval(node.value)
    raise RuntimeError("Could not find default_pip_packages in DefaultConfig.py")


setup(name='blenderproc',
    version=version['__version__'],
    url='https://github.com/DLR-RM/BlenderProc',
    author='Maximilian Denninger, Dominik Winkelbauer, Martin Sundermeyer',
    maintainer='Dominik Winkelbauer',
    packages=find_packages(exclude=['docs', 'examples', 'external', 'images', 'resources', 'scripts', 'tests']),
    include_package_data=True,
    entry_points={
        'console_scripts': ['blenderproc=blenderproc.command_line:cli'],
    },      
    install_requires=["setuptools", "pyyaml", "requests", "matplotlib", "numpy", "Pillow", "h5py", "progressbar"],
    # "pip install blenderproc[bpy]" installs Blender as a python module, so BlenderProc runs in any python 3.13
    # environment (e.g. a venv) without downloading a separate Blender installation
    extras_require={
        "bpy": [f"bpy=={bpy_version}"] + [package for package in read_default_pip_packages() if package != "wheel"],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
