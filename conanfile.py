from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout


class Coin3dTestConan(ConanFile):
    name = "coin3d_test"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Coin3dTest here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    requires = "qt/5.15.6"

    options = {
        "shared": [True, False],
        "fPIC": [True, False]

    }

    default_options = {
        "shared": False,
        "fPIC": True,
        # "qt:with_openal": False,
        # "qt:with_odbc": False,
        # "qt:with_pq": False,
        # "qt:with_mysql": False,
        # "qt:with_sqlite3": False,
        #"qt:qtwayland": True
                               "qt:opengl": "no",
                       "qt:openssl": False,
                       "qt:with_pcre2": True,
                       "qt:with_freetype": True,
                       "qt:with_fontconfig": True,
                       "qt:with_icu": True,
                       "qt:with_libjpeg": "False",
                       "qt:with_libpng": False,
                       "qt:with_sqlite3": False,
                       "qt:with_mysql": False,
                       "qt:with_pq": False,
                       "qt:with_odbc": False,
                       "qt:with_openal": False,
                       "qt:with_zstd": True,
                       "qt:with_md4c": False,
                       "qt:gui": True,
                       "qt:widgets": True,
    }

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
