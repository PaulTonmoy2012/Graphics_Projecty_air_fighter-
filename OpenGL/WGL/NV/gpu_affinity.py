'''OpenGL extension NV.gpu_affinity

This module customises the behaviour of the 
OpenGL.raw.WGL.NV.gpu_affinity to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/gpu_affinity.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.WGL import _types, _glgets
from OpenGL.raw.WGL.NV.gpu_affinity import *
from OpenGL.raw.WGL.NV.gpu_affinity import _EXTENSION_NAME

def glInitGpuAffinityNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION