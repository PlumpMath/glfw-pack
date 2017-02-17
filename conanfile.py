from conans import ConanFile, CMake, tools
import sys
import os

class glfw3(ConanFile):
    name    = "glfw"
    description = "An Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan application development"
    version = "3.2.1"
    url = "https://github.com/nbarrett93/glfw-pack"
    license = "zlib/libpng"

    settings = "os", "compiler", "build_type", "arch"

    options = { 
            "shared" : [True, False]
            }
    default_options = "shared=False"

    origin = "https://github.com/glfw/glfw"

    def source(self):
        self.run("git clone {}".format(self.origin))
        self.run("git checkout tags/{}".format(self.version), cwd="glfw")

    def build(self):
        cmake = CMake(self.settings)

        args  = ["-DBUILD_SHARED_LIBS=ON" if self.options.shared else "-DBUILD_SHARED_LIBS=OFF"]
        args += ["-DGLFW_BUILD_DOCS=OFF"]
        args += ["-DGLFW_BUILD_EXAMPLES=OFF"]
        args += ["-DGLFW_BUILD_TESTS=OFF"]
        args += ["-DGLFW_INSTALL=ON"]
        args += ["-DCMAKE_INSTALL_PREFIX={}".format(self.package_folder)]

        self.run('cmake {}/glfw {} {}'
                 .format(self.conanfile_directory, cmake.command_line, ' '.join(args)))
        self.run('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = [ 
                "glfw3", "rt", "m" ,"dl" ,"Xrandr" ,
                "Xinerama", "Xxf86vm" ,"Xext" ,"Xcursor", 
                "Xrender" ,"Xfixes", "X11", "pthread", 
                "xcb" ,"Xau", "Xdmcp", "GL"
                ]
