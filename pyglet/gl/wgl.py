# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2019 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for C:\cygwin\home\Alex\pyglet\tools\wgl.h

Generated by tools/gengl.py.
Do not modify this file.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: gengl.py 601 2007-02-04 05:36:59Z Alex.Holkner $'

from ctypes import *
from pyglet.gl.lib import link_WGL as _link_function
from pyglet.gl.lib import c_ptrdiff_t

if not _link_function:
    raise ImportError('opengl32.dll is not available.')

# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by tools/gengl.py.
# Wrapper for C:\cygwin\home\Alex\pyglet\tools\wgl.h


CONST = 0 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:14
GLenum = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:17
GLboolean = c_ubyte 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:18
GLbitfield = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:19
GLbyte = c_char 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:20
GLshort = c_short 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:21
GLint = c_int 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:22
GLsizei = c_int 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:23
GLubyte = c_ubyte 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:24
GLushort = c_ushort 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:25
GLuint = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:26
GLfloat = c_float 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:27
GLclampf = c_float 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:28
GLdouble = c_double 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:29
GLclampd = c_double 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:30
GLvoid = None 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:31
INT8 = c_char 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:33
PINT8 = c_char_p 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:33
INT16 = c_short 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:34
PINT16 = POINTER(c_short) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:34
INT32 = c_int 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:35
PINT32 = POINTER(c_int) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:35
UINT8 = c_ubyte 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:36
PUINT8 = POINTER(c_ubyte) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:36
UINT16 = c_ushort 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:37
PUINT16 = POINTER(c_ushort) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:37
UINT32 = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:38
PUINT32 = POINTER(c_uint) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:38
LONG32 = c_int 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:39
PLONG32 = POINTER(c_int) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:39
ULONG32 = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:40
PULONG32 = POINTER(c_uint) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:40
DWORD32 = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:41
PDWORD32 = POINTER(c_uint) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:41
INT64 = c_longlong 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:42
PINT64 = POINTER(c_longlong) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:42
UINT64 = c_ulonglong 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:43
PUINT64 = POINTER(c_ulonglong) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:43
VOID = None 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:45
LPVOID = POINTER(None) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:45
LPCSTR = c_char_p 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:46
CHAR = c_char 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:47
BYTE = c_ubyte 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:48
WORD = c_ushort 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:49
USHORT = c_ushort 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:49
UINT = c_uint 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:50
INT = c_int 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:51
INT_PTR = POINTER(c_int) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:51
BOOL = c_long 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:52
LONG = c_long 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:53
DWORD = c_ulong 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:54
FLOAT = c_float 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:55
COLORREF = DWORD 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:56
LPCOLORREF = POINTER(DWORD) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:56
HANDLE = POINTER(None) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:58
HGLRC = HANDLE 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:60
HDC = HANDLE 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:61
PROC = CFUNCTYPE(INT_PTR) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:63
# C:\cygwin\home\Alex\pyglet\tools\wgl.h:65
wglCopyContext = _link_function('wglCopyContext', BOOL, [HGLRC, HGLRC, UINT], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:66
wglCreateContext = _link_function('wglCreateContext', HGLRC, [HDC], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:67
wglCreateLayerContext = _link_function('wglCreateLayerContext', HGLRC, [HDC, c_int], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:68
wglDeleteContext = _link_function('wglDeleteContext', BOOL, [HGLRC], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:69
wglGetCurrentContext = _link_function('wglGetCurrentContext', HGLRC, [], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:70
wglGetCurrentDC = _link_function('wglGetCurrentDC', HDC, [], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:71
wglGetProcAddress = _link_function('wglGetProcAddress', PROC, [LPCSTR], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:72
wglMakeCurrent = _link_function('wglMakeCurrent', BOOL, [HDC, HGLRC], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:73
wglShareLists = _link_function('wglShareLists', BOOL, [HGLRC, HGLRC], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:74
wglUseFontBitmapsA = _link_function('wglUseFontBitmapsA', BOOL, [HDC, DWORD, DWORD, DWORD], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:75
wglUseFontBitmapsW = _link_function('wglUseFontBitmapsW', BOOL, [HDC, DWORD, DWORD, DWORD], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:76
SwapBuffers = _link_function('SwapBuffers', BOOL, [HDC], None)

class struct__POINTFLOAT(Structure):
    __slots__ = [
        'x',
        'y',
    ]
struct__POINTFLOAT._fields_ = [
    ('x', FLOAT),
    ('y', FLOAT),
]

POINTFLOAT = struct__POINTFLOAT 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:81
PPOINTFLOAT = POINTER(struct__POINTFLOAT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:81
class struct__GLYPHMETRICSFLOAT(Structure):
    __slots__ = [
        'gmfBlackBoxX',
        'gmfBlackBoxY',
        'gmfptGlyphOrigin',
        'gmfCellIncX',
        'gmfCellIncY',
    ]
struct__GLYPHMETRICSFLOAT._fields_ = [
    ('gmfBlackBoxX', FLOAT),
    ('gmfBlackBoxY', FLOAT),
    ('gmfptGlyphOrigin', POINTFLOAT),
    ('gmfCellIncX', FLOAT),
    ('gmfCellIncY', FLOAT),
]

GLYPHMETRICSFLOAT = struct__GLYPHMETRICSFLOAT 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:89
PGLYPHMETRICSFLOAT = POINTER(struct__GLYPHMETRICSFLOAT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:89
LPGLYPHMETRICSFLOAT = POINTER(struct__GLYPHMETRICSFLOAT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:89
WGL_FONT_LINES = 0 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:91
WGL_FONT_POLYGONS = 1 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:92
# C:\cygwin\home\Alex\pyglet\tools\wgl.h:93
wglUseFontOutlinesA = _link_function('wglUseFontOutlinesA', BOOL, [HDC, DWORD, DWORD, DWORD, FLOAT, FLOAT, c_int, LPGLYPHMETRICSFLOAT], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:95
wglUseFontOutlinesW = _link_function('wglUseFontOutlinesW', BOOL, [HDC, DWORD, DWORD, DWORD, FLOAT, FLOAT, c_int, LPGLYPHMETRICSFLOAT], None)

class struct_tagLAYERPLANEDESCRIPTOR(Structure):
    __slots__ = [
        'nSize',
        'nVersion',
        'dwFlags',
        'iPixelType',
        'cColorBits',
        'cRedBits',
        'cRedShift',
        'cGreenBits',
        'cGreenShift',
        'cBlueBits',
        'cBlueShift',
        'cAlphaBits',
        'cAlphaShift',
        'cAccumBits',
        'cAccumRedBits',
        'cAccumGreenBits',
        'cAccumBlueBits',
        'cAccumAlphaBits',
        'cDepthBits',
        'cStencilBits',
        'cAuxBuffers',
        'iLayerPlane',
        'bReserved',
        'crTransparent',
    ]
struct_tagLAYERPLANEDESCRIPTOR._fields_ = [
    ('nSize', WORD),
    ('nVersion', WORD),
    ('dwFlags', DWORD),
    ('iPixelType', BYTE),
    ('cColorBits', BYTE),
    ('cRedBits', BYTE),
    ('cRedShift', BYTE),
    ('cGreenBits', BYTE),
    ('cGreenShift', BYTE),
    ('cBlueBits', BYTE),
    ('cBlueShift', BYTE),
    ('cAlphaBits', BYTE),
    ('cAlphaShift', BYTE),
    ('cAccumBits', BYTE),
    ('cAccumRedBits', BYTE),
    ('cAccumGreenBits', BYTE),
    ('cAccumBlueBits', BYTE),
    ('cAccumAlphaBits', BYTE),
    ('cDepthBits', BYTE),
    ('cStencilBits', BYTE),
    ('cAuxBuffers', BYTE),
    ('iLayerPlane', BYTE),
    ('bReserved', BYTE),
    ('crTransparent', COLORREF),
]

LAYERPLANEDESCRIPTOR = struct_tagLAYERPLANEDESCRIPTOR 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:125
PLAYERPLANEDESCRIPTOR = POINTER(struct_tagLAYERPLANEDESCRIPTOR) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:125
LPLAYERPLANEDESCRIPTOR = POINTER(struct_tagLAYERPLANEDESCRIPTOR) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:125
LPD_DOUBLEBUFFER = 1 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:128
LPD_STEREO = 2 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:129
LPD_SUPPORT_GDI = 16 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:130
LPD_SUPPORT_OPENGL = 32 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:131
LPD_SHARE_DEPTH = 64 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:132
LPD_SHARE_STENCIL = 128 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:133
LPD_SHARE_ACCUM = 256 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:134
LPD_SWAP_EXCHANGE = 512 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:135
LPD_SWAP_COPY = 1024 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:136
LPD_TRANSPARENT = 4096 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:137
LPD_TYPE_RGBA = 0 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:139
LPD_TYPE_COLORINDEX = 1 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:140
WGL_SWAP_MAIN_PLANE = 1 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:143
WGL_SWAP_OVERLAY1 = 2 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:144
WGL_SWAP_OVERLAY2 = 4 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:145
WGL_SWAP_OVERLAY3 = 8 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:146
WGL_SWAP_OVERLAY4 = 16 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:147
WGL_SWAP_OVERLAY5 = 32 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:148
WGL_SWAP_OVERLAY6 = 64 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:149
WGL_SWAP_OVERLAY7 = 128 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:150
WGL_SWAP_OVERLAY8 = 256 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:151
WGL_SWAP_OVERLAY9 = 512 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:152
WGL_SWAP_OVERLAY10 = 1024 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:153
WGL_SWAP_OVERLAY11 = 2048 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:154
WGL_SWAP_OVERLAY12 = 4096 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:155
WGL_SWAP_OVERLAY13 = 8192 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:156
WGL_SWAP_OVERLAY14 = 16384 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:157
WGL_SWAP_OVERLAY15 = 32768 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:158
WGL_SWAP_UNDERLAY1 = 65536 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:159
WGL_SWAP_UNDERLAY2 = 131072 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:160
WGL_SWAP_UNDERLAY3 = 262144 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:161
WGL_SWAP_UNDERLAY4 = 524288 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:162
WGL_SWAP_UNDERLAY5 = 1048576 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:163
WGL_SWAP_UNDERLAY6 = 2097152 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:164
WGL_SWAP_UNDERLAY7 = 4194304 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:165
WGL_SWAP_UNDERLAY8 = 8388608 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:166
WGL_SWAP_UNDERLAY9 = 16777216 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:167
WGL_SWAP_UNDERLAY10 = 33554432 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:168
WGL_SWAP_UNDERLAY11 = 67108864 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:169
WGL_SWAP_UNDERLAY12 = 134217728 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:170
WGL_SWAP_UNDERLAY13 = 268435456 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:171
WGL_SWAP_UNDERLAY14 = 536870912 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:172
WGL_SWAP_UNDERLAY15 = 1073741824 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:173
# C:\cygwin\home\Alex\pyglet\tools\wgl.h:175
wglDescribeLayerPlane = _link_function('wglDescribeLayerPlane', BOOL, [HDC, c_int, c_int, UINT, LPLAYERPLANEDESCRIPTOR], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:177
wglSetLayerPaletteEntries = _link_function('wglSetLayerPaletteEntries', c_int, [HDC, c_int, c_int, c_int, POINTER(COLORREF)], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:179
wglGetLayerPaletteEntries = _link_function('wglGetLayerPaletteEntries', c_int, [HDC, c_int, c_int, c_int, POINTER(COLORREF)], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:181
wglRealizeLayerPalette = _link_function('wglRealizeLayerPalette', BOOL, [HDC, c_int, BOOL], None)

# C:\cygwin\home\Alex\pyglet\tools\wgl.h:182
wglSwapLayerBuffers = _link_function('wglSwapLayerBuffers', BOOL, [HDC, UINT], None)

class struct__WGLSWAP(Structure):
    __slots__ = [
        'hdc',
        'uiFlags',
    ]
struct__WGLSWAP._fields_ = [
    ('hdc', HDC),
    ('uiFlags', UINT),
]

WGLSWAP = struct__WGLSWAP 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:188
PWGLSWAP = POINTER(struct__WGLSWAP) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:188
LPWGLSWAP = POINTER(struct__WGLSWAP) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:188
WGL_SWAPMULTIPLE_MAX = 16 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:190
# C:\cygwin\home\Alex\pyglet\tools\wgl.h:192
wglSwapMultipleBuffers = _link_function('wglSwapMultipleBuffers', DWORD, [UINT, POINTER(WGLSWAP)], None)

class struct_tagRECT(Structure):
    __slots__ = [
        'left',
        'top',
        'right',
        'bottom',
    ]
struct_tagRECT._fields_ = [
    ('left', LONG),
    ('top', LONG),
    ('right', LONG),
    ('bottom', LONG),
]

RECT = struct_tagRECT 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:200
PRECT = POINTER(struct_tagRECT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:200
NPRECT = POINTER(struct_tagRECT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:200
LPRECT = POINTER(struct_tagRECT) 	# C:\cygwin\home\Alex\pyglet\tools\wgl.h:200

__all__ = ['CONST', 'GLenum', 'GLboolean', 'GLbitfield', 'GLbyte', 'GLshort',
'GLint', 'GLsizei', 'GLubyte', 'GLushort', 'GLuint', 'GLfloat', 'GLclampf',
'GLdouble', 'GLclampd', 'GLvoid', 'INT8', 'PINT8', 'INT16', 'PINT16', 'INT32',
'PINT32', 'UINT8', 'PUINT8', 'UINT16', 'PUINT16', 'UINT32', 'PUINT32',
'LONG32', 'PLONG32', 'ULONG32', 'PULONG32', 'DWORD32', 'PDWORD32', 'INT64',
'PINT64', 'UINT64', 'PUINT64', 'VOID', 'LPVOID', 'LPCSTR', 'CHAR', 'BYTE',
'WORD', 'USHORT', 'UINT', 'INT', 'INT_PTR', 'BOOL', 'LONG', 'DWORD', 'FLOAT',
'COLORREF', 'LPCOLORREF', 'HANDLE', 'HGLRC', 'HDC', 'PROC', 'wglCopyContext',
'wglCreateContext', 'wglCreateLayerContext', 'wglDeleteContext',
'wglGetCurrentContext', 'wglGetCurrentDC', 'wglGetProcAddress',
'wglMakeCurrent', 'wglShareLists', 'wglUseFontBitmapsA', 'wglUseFontBitmapsW',
'SwapBuffers', 'POINTFLOAT', 'PPOINTFLOAT', 'GLYPHMETRICSFLOAT',
'PGLYPHMETRICSFLOAT', 'LPGLYPHMETRICSFLOAT', 'WGL_FONT_LINES',
'WGL_FONT_POLYGONS', 'wglUseFontOutlinesA', 'wglUseFontOutlinesW',
'LAYERPLANEDESCRIPTOR', 'PLAYERPLANEDESCRIPTOR', 'LPLAYERPLANEDESCRIPTOR',
'LPD_DOUBLEBUFFER', 'LPD_STEREO', 'LPD_SUPPORT_GDI', 'LPD_SUPPORT_OPENGL',
'LPD_SHARE_DEPTH', 'LPD_SHARE_STENCIL', 'LPD_SHARE_ACCUM',
'LPD_SWAP_EXCHANGE', 'LPD_SWAP_COPY', 'LPD_TRANSPARENT', 'LPD_TYPE_RGBA',
'LPD_TYPE_COLORINDEX', 'WGL_SWAP_MAIN_PLANE', 'WGL_SWAP_OVERLAY1',
'WGL_SWAP_OVERLAY2', 'WGL_SWAP_OVERLAY3', 'WGL_SWAP_OVERLAY4',
'WGL_SWAP_OVERLAY5', 'WGL_SWAP_OVERLAY6', 'WGL_SWAP_OVERLAY7',
'WGL_SWAP_OVERLAY8', 'WGL_SWAP_OVERLAY9', 'WGL_SWAP_OVERLAY10',
'WGL_SWAP_OVERLAY11', 'WGL_SWAP_OVERLAY12', 'WGL_SWAP_OVERLAY13',
'WGL_SWAP_OVERLAY14', 'WGL_SWAP_OVERLAY15', 'WGL_SWAP_UNDERLAY1',
'WGL_SWAP_UNDERLAY2', 'WGL_SWAP_UNDERLAY3', 'WGL_SWAP_UNDERLAY4',
'WGL_SWAP_UNDERLAY5', 'WGL_SWAP_UNDERLAY6', 'WGL_SWAP_UNDERLAY7',
'WGL_SWAP_UNDERLAY8', 'WGL_SWAP_UNDERLAY9', 'WGL_SWAP_UNDERLAY10',
'WGL_SWAP_UNDERLAY11', 'WGL_SWAP_UNDERLAY12', 'WGL_SWAP_UNDERLAY13',
'WGL_SWAP_UNDERLAY14', 'WGL_SWAP_UNDERLAY15', 'wglDescribeLayerPlane',
'wglSetLayerPaletteEntries', 'wglGetLayerPaletteEntries',
'wglRealizeLayerPalette', 'wglSwapLayerBuffers', 'WGLSWAP', 'PWGLSWAP',
'LPWGLSWAP', 'WGL_SWAPMULTIPLE_MAX', 'wglSwapMultipleBuffers', 'RECT',
'PRECT', 'NPRECT', 'LPRECT']
# END GENERATED CONTENT (do not edit above this line)

