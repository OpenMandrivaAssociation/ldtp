Summary: Linux Desktop Testing Project
Name:    ldtp
Version: 2.0.5
Release: %mkrel 1
License: GPLv2+/LGPLv2.1+
Group:   Graphical desktop/Other
URL:     http://ldtp.freedesktop.org/
Source0: http://download.freedesktop.org/ldtp/1.x/1.xi76.x/%name-%version.tar.gz
BuildRoot: %_tmppath/%name-root
BuildRequires: at-spi-devel python

%description
GNU/Linux Desktop Testing Project (GNU/LDTP) is aimed at producing high quality
test automation framework and cutting-edge tools that can be used to test
GNU/Linux Desktop and improve it. It uses the Accessibility libraries to poke
through the applications user interface. The framework has tools to generate
Appmap by reading through the user interface components of an application. The
framework also has tools to record test-cases based on user-selection on the
application.

GNU/LDTP core framework uses Appmap and the recorded test-cases to test an
application and gives the status of each test-case as output. As of now,
GNU/LDTP can test any GNOME application which are accessibility enabled,
Mozilla, Openoffice.org, any Java application (should have a UI based on swing)
and KDE 4.0 applications based on QT 4.0 (based on the press releases by KDE).

We encourage you to join the project and help us to create robust, reliable and
stable test tool/framework for Unix Desktops. 

%prep
%setup

%build

%{__python} setup.py build

%install
rm -fr $RPM_BUILD_ROOT

%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING 
%{_bindir}/*
%py_platsitedir/*

