# Script generated with Bloom
pkgdesc="ROS - Basic diagnostic_aggregator tests are in the"
url='http://ros.org/wiki/test_diagnostic_aggregator'

pkgname='ros-lunar-test-diagnostic-aggregator'
pkgver='1.9.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-diagnostic-aggregator>=1.8.9'
'ros-lunar-diagnostic-msgs'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-rostest'
)

depends=('ros-lunar-diagnostic-aggregator>=1.8.9'
'ros-lunar-diagnostic-msgs'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-rospy'
)

conflicts=()
replaces=()

_dir=test_diagnostic_aggregator
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_diagnostic_aggregator $srcdir/test_diagnostic_aggregator
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

