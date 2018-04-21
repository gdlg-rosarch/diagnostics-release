# Script generated with Bloom
pkgdesc="ROS - The diagnostic_analysis package can convert a log of diagnostics data into a series of CSV files. Robot logs are recorded with rosbag, and can be processed offline using the scripts in this package."
url='http://www.ros.org/wiki/diagnostics_analysis'

pkgname='ros-lunar-diagnostic-analysis'
pkgver='1.9.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.68'
'ros-lunar-diagnostic-msgs'
'ros-lunar-rosbag'
'ros-lunar-roslib'
'ros-lunar-rostest'
)

depends=('ros-lunar-diagnostic-msgs'
'ros-lunar-rosbag'
'ros-lunar-roslib'
)

conflicts=()
replaces=()

_dir=diagnostic_analysis
source=()
md5sums=()

prepare() {
    cp -R $startdir/diagnostic_analysis $srcdir/diagnostic_analysis
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

