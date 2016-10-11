from conans import ConanFile, ConfigureEnvironment
from conans.tools import get, os_info
import shutil

class OnigmoConan(ConanFile):
    name = "Onigmo"
    version = "5.15.0"
    ZIP_FOLDER_NAME = "Onigmo-Onigmo-5.15.0"
    license = 'https://github.com/k-takata/Onigmo/blob/master/COPYING'
    url = "http://github.com/shinichy/conan-onigmo"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        url = "https://github.com/k-takata/Onigmo/archive/Onigmo-%s.zip" % self.version
        get(url)

    def build(self):
        if os_info.is_windows:
            self.build_windows()
        else:
            self.build_with_configure()

    def build_windows(self):
        shutil.copy( '%s/win32/Makefile' % self.ZIP_FOLDER_NAME, '%s' % self.ZIP_FOLDER_NAME )
        shutil.copy( '%s/win32/config.h' % self.ZIP_FOLDER_NAME, '%s' % self.ZIP_FOLDER_NAME )
        self.run("cd %s & nmake" % self.ZIP_FOLDER_NAME)

    def build_with_configure(self):
        flags = '--prefix=%s' % self.package_folder
        env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
        self.run("cd %s && chmod +x configure install-sh" % self.ZIP_FOLDER_NAME)
        self.run("cd %s && %s ./configure %s" % (self.ZIP_FOLDER_NAME, env.command_line, flags))
        self.run("cd %s && %s make" % (self.ZIP_FOLDER_NAME, env.command_line))
        self.run("cd %s && %s make install" % (self.ZIP_FOLDER_NAME, env.command_line))

    def package(self):
        self.copy( '*.h', dst='include', keep_path=False )
        self.copy( '*onig*.lib', dst='lib', keep_path=False )
        self.copy( '*onig*.dll', dst='bin', keep_path=False )
        self.copy( '*onig*.so', dst='lib', keep_path=False )
        self.copy( '*onig*.a', dst='lib', keep_path=False )
        self.copy( '*onig*.dylib', dst='lib', keep_path=False )

    def package_info(self):
        self.cpp_info.libs = ["onig"]
