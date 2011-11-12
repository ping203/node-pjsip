# -*- Python -*-

import os;

#target='i686-pc-linux-gnu'
target='x86_64-unknown-linux-gnu'
libs = [ lib + '-' + target for lib in
         [ 'pjsua', 'pjsip-ua', 'pjsip-simple', 'pjsip', 'pjmedia-codec', 'pjmedia',
           'pjmedia-audiodev', 'pjnath', 'pjlib-util', 'resample', 'milenage', 'srtp',
           'gsmcodec', 'speex', 'ilbccodec', 'portaudio', 'pj' ]
         ] + ['m', 'nsl', 'rt', 'pthread', 'asound']


def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall", "-I.." ]
  obj.libs = libs
  obj.target = "pjsip"
  obj.source = "pjsip.cc"