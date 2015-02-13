Name:           ros-jade-diagnostic-analysis
Version:        1.8.7
Release:        0%{?dist}
Summary:        ROS diagnostic_analysis package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/diagnostics_analysis
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-rosbag
Requires:       ros-jade-roslib
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rostest

%description
The diagnostic_analysis package can convert a log of diagnostics data into a
series of CSV files. Robot logs are recorded with rosbag, and can be processed
offline using the scripts in this package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Feb 12 2015 Austin Hendrix <namniart@gmail.com> - 1.8.7-0
- Autogenerated by Bloom

