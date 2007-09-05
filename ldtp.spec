Summary: Linux Desktop Testing Project
Name:    ldtp
Version: 0.9.0
Release: %mkrel 2
License: LGPL
Group:   Graphical desktop/Other
URL:     http://ldtp.freedesktop.org/
Source0:  %name-%version.tar.bz2
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
%configure2_5x --disable-debug
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_bindir}/*
%py_platsitedir/*
