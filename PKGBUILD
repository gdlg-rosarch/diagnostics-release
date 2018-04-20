# Script generated with Bloom
pkgdesc="ROS - diagnostic_aggregator"
url='http://www.ros.org/wiki/diagnostic_aggregator'

pkgname='ros-kinetic-diagnostic-aggregator'
pkgver='1.9.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-bondcpp'
'ros-kinetic-bondpy'
'ros-kinetic-catkin>=0.5.68'
'ros-kinetic-diagnostic-msgs>=1.11.9'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rostest'
'ros-kinetic-xmlrpcpp'
)

depends=('ros-kinetic-bondcpp'
'ros-kinetic-bondpy'
'ros-kinetic-diagnostic-msgs>=1.11.9'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=diagnostic_aggregator
source=()
md5sums=()

prepare() {
    cp -R $startdir/diagnostic_aggregator $srcdir/diagnostic_aggregator
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

