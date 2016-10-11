# conan-Onigmo
[Conan](https://conan.io) package for the Onigmo library (https://github.com/k-takata/Onigmo).

[![badge](https://img.shields.io/badge/conan.io-Onigmo%2F57.1-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/Onigmo/57.1/shinichy/stable)

[![Build Status](https://travis-ci.org/shinichy/conan-onigmo.svg?branch=master)](https://travis-ci.org/shinichy/conan-onigmo)
[![Build status](https://ci.appveyor.com/api/projects/status/m5clq0qwkt36x5w7?svg=true)](https://ci.appveyor.com/project/shinichy/conan-Onigmo)

## Example

The following example shows how to use this Conan package with CMake.  See Conan's
documentation for other generators if you are not using CMake.

Add the package to your project's *conanfile.txt*:

```
[requires]
Onigmo/5.15.0@shinichy/stable

[generators]
cmake
```

Your *CMakeLists.txt*:

```CMake
project(tst_Onigmo)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_output_dirs_setup()

add_executable(tst_Onigmo Onigmo.cpp)
target_link_libraries(tst_Onigmo ${CONAN_LIBS})
```

And then your *example.cpp*:

```cpp
#include "oniguruma.h"

int main(int argc, char* argv[])
{
  int r;
  unsigned char *start, *range, *end;
  regex_t* reg;
  OnigErrorInfo einfo;
  OnigRegion *region;

  static UChar* pattern = (UChar* )"a(.*)b|[e-f]+";
  static UChar* str     = (UChar* )"zzzzaffffffffb";

  r = onig_new(&reg, pattern, pattern + strlen((char* )pattern),
  ...
}
```

Then you can use it as:

```bash
$ mkdir build && cd build
$ conan install ..
$ cmake .. -G "Visual Studio 14 Win64"
$ cmake --build . --config Release
$ bin/example
```