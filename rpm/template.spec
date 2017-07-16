Name:           ros-lunar-diagnostic-updater
Version:        1.9.1
Release:        0%{?dist}
Summary:        ROS diagnostic_updater package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/diagnostic_updater
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-diagnostic-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-diagnostic-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-std-msgs

%description
diagnostic_updater contains tools for easily updating diagnostics. it is
commonly used in device drivers to keep track of the status of output topics,
device status, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Jul 15 2017 Austin Hendrix <namniart@gmail.com> - 1.9.1-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Austin Hendrix <namniart@gmail.com> - 1.9.0-0
- Autogenerated by Bloom

