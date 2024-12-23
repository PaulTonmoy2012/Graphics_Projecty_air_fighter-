'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_draw_vulkan_image'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_draw_vulkan_image',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLuint64,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glDrawVkImageNV(vkImage,sampler,x0,y0,x1,y1,z,s0,t0,s1,t1):pass
@_f
@_p.types(_cs.GLVULKANPROCNV,arrays.GLcharArray)
def glGetVkProcAddrNV(name):pass
@_f
@_p.types(None,_cs.GLuint64)
def glSignalVkFenceNV(vkFence):pass
@_f
@_p.types(None,_cs.GLuint64)
def glSignalVkSemaphoreNV(vkSemaphore):pass
@_f
@_p.types(None,_cs.GLuint64)
def glWaitVkSemaphoreNV(vkSemaphore):pass
