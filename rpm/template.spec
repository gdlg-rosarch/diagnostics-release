Name:           ros-indigo-test-diagnostic-aggregator
Version:        1.8.8
Release:        0%{?dist}
Summary:        ROS test_diagnostic_aggregator package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/test_diagnostic_aggregator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-aggregator
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest

%description
Basic diagnostic_aggregator tests are in the

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Aug 06 2015 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.8-0
- Autogenerated by Bloom

* Fri Jan 09 2015 Brice Rebsamen <brice.rebsamen@gmail.com> - 1.8.7-0
- Autogenerated by Bloom

