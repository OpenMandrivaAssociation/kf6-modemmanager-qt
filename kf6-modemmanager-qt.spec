%define libname %mklibname KF6ModemManagerQt
%define devname %mklibname KF6ModemManagerQt -d
%define git 20230609

Name: kf6-modemmanager-qt
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/modemmanager-qt/-/archive/master/modemmanager-qt-master.tar.bz2#/modemmanager-qt-%{git}.tar.bz2
Summary: Qt wrapper for the ModemManager DBus API
URL: https://invent.kde.org/frameworks/modemmanager-qt
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Xml)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: pkgconfig(ModemManager)
Requires: %{libname} = %{EVRD}

%description
Qt wrapper for the ModemManager DBus API

%package -n %{libname}
Summary: Qt wrapper for the ModemManager DBus API
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt wrapper for the ModemManager DBus API

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: pkgconfig(ModemManager)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt wrapper for the ModemManager DBus API

%prep
%autosetup -p1 -n modemmanager-qt-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/ModemManagerQt
%{_libdir}/cmake/KF6ModemManagerQt
%{_libdir}/qt6/doc/KF6ModemManagerQt.*

%files -n %{libname}
%{_libdir}/libKF6ModemManagerQt.so*
