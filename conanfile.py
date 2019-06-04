from conans import ConanFile, tools
import os

class OUIBlendishConan(ConanFile):
    name = "OUIBlendishVCVRack"
    version = "latest"
    license = "MIT"
    author = "Leonard Ritter, Andrew Belt"
    url = "https://github.com/qno/conan-andrewbelt-oui-blendish"
    homepage = "https://github.com/AndrewBelt/oui-blendish"
    description = "Blendish [VCVRack fork] - Blender 2.5 UI based theming functions for NanoVG."

    no_copy_source = True

    _pkg_name = "oui-blendish-master"

    def requirements(self):
        self.requires.add("NanoVG/latest@qno/testing")

    def source(self):
        url = "https://github.com/AndrewBelt/oui-blendish/archive/master.zip"
        self.output.info("Downloading {}".format(url))
        tools.get(url)

    def package(self):
        self.copy("*.h", dst="include", src=self._pkg_name)

    def package_id(self):
        self.info.header_only()
