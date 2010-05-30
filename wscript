#!/usr/bin/env python
APPNAME = "VaEdit"
VERSION = "0.1"

top = "."
out = "build"

def set_options(opt):
	opt.tool_options('compiler_cc')
	opt.tool_options('vala')

def configure(conf):
	conf.check_tool('compiler_cc cc vala')
	conf.check_cfg(package='glib-2.0',uselib_store='GLIB',atleast_version='2.10.0',mandatory=1,args='--cflags --libs')
	conf.check_cfg(package='gtk+-2.0',uselib_store='GTK',atleast_version='2.10.0',mandatory=1,args='--cflags --libs')
	conf.check_cfg(package='gtksourceview-2.0',uselib_store='GTKSOURCEVIEW',atleast_version='2.10.0',mandatory=1,args='--cflags --libs')
	conf.check_cfg(package='gio-2.0',uselib_store='GIO',atleast_version='2.10.0',mandatory=1,args='--cflags --libs')
	conf.check_cfg(package='gee-1.0',uselib_store='GEE',atleast_version='0.5.0',mandatory=1,args='--cflags --libs')
	conf.define('GETTEXT_PACKAGE','VaEdit')
	conf.write_config_header('config.h')
	
def build(bld):
	bld.add_subdirs('src')
