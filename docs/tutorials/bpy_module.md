# Using `bpy` module from pip

BlenderProc supports using the `bpy` module installed from pip, e.g. inside of a virtual environment. Then no separate Blender installation is downloaded, and scripts are executed by the python interpreter of your environment.

## Setup

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install "blenderproc[bpy]"      # or, inside of a clone of this repository: pip install ".[bpy]"
```

The `bpy` extra installs `bpy==5.2.3` together with all python packages BlenderProc needs.
Afterwards, run your script using `python my_script.py` or `blenderproc run my_script.py` (after `import blenderproc`, call `blenderproc.init()` as usual).

BlenderProc automatically uses the `bpy` module, if it is installed in the current python environment.
This can be controlled via the `USE_EXTERNAL_BPY_MODULE` environment variable:
- `USE_EXTERNAL_BPY_MODULE=1`: always use the `bpy` module from the environment (fails, if it is not installed).
- `USE_EXTERNAL_BPY_MODULE=0`: always use BlenderProc's own Blender installation, even if `bpy` is installed.

## Limitations
- **Requires Python** version **3.13** - this is bound to the version `bpy` and Blender uses, it is the Python version suggested by [VFX Reference Platform](https://vfxplatform.com/).
- All [limitations](https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html#limitations) of the `bpy` module itself.
- `blenderproc debug` command is not available, as `bpy` module does not support user interface.
- `blenderproc pip` commands are not available. Use the `pip` commands in your environment instead.
- Some loaders and writers need additional packages, which are not installed by the `bpy` extra. If one is missing, BlenderProc prints the `pip install` command for it, e.g. `pip install urchin` for the URDF loader or `pip install git+https://github.com/thodan/bop_toolkit PyOpenGL==3.1.0` for the BOP writer.

## Required dependencies
If you prefer to install the dependencies manually instead of using the `bpy` extra, these are needed next to BlenderProc itself:

```
pip install wheel bpy==5.2.3 pyyaml==6.0.2 imageio==2.37.0 gitpython==3.1.44 scikit-image==0.25.2 pypng==0.20220715.0 scipy==1.15.3 matplotlib==3.10.3 pytz==2025.2 h5py==3.14.0 Pillow==11.2.1 opencv-contrib-python==4.11.* scikit-learn==1.7.0 python-dateutil==2.9.0.post0 rich==14.0.0 trimesh==4.6.12 pyrender==0.1.45 PyQT5
```

This is because BlenderProc does not require these dependencies directly, but the Blender it uses does. When using `bpy` package there is no Blender being installed and these dependencies become dependencies of the BlenderProc.

## Troubleshooting

### Python version mismatch

```
pip install bpy==5.2.3
Defaulting to user installation because normal site-packages is not writeable
ERROR: Ignored the following versions that require a different python version: 2.82.1 Requires-Python >=3.7, <3.8
ERROR: Could not find a version that satisfies the requirement bpy==5.2.3 (from versions: none)
ERROR: No matching distribution found for bpy==5.2.3
```

Using BlenderProc with `bpy` module from pip strictly requires Python3.13, see [Limitations](#limitations). Suggested workflow is to work with virtual environment using Python3.13. 

```
python --version
Python 3.13 X

python -m venv "venv"
```

Then continue with the [Setup](#setup).
