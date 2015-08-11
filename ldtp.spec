Summary: Linux Desktop Testing Project
Name:    ldtp
Version: 3.5.0
Release: 2
License: LGPL
Group:   Graphical desktop/Other
URL:     http://ldtp.freedesktop.org/
Source0: http://download.freedesktop.org/ldtp/1.x/1.xi76.x/%name-%version.tar.gz
BuildRoot: %_tmppath/%name-root
BuildArch: noarch
BuildRequires: python
Requires: python-gobject
Requires: pyatspi
Requires: typelib(Wnck) = 3.0
Requires: typelib(Gtk) = 3.0
Requires: typelib(Gdk) = 3.0
Requires: python-twisted-core

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
%setup -q

%build

%{__python} setup.py build

%install
rm -fr $RPM_BUILD_ROOT

%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING examples/
%{_bindir}/*
%py_puresitedir/*


%changelog
* Sat Nov 13 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 2.0.6-2mdv2011.0
+ Revision: 597027
- added missing deps and buildrequires
- fixed license
- added examples/ in documentation

* Thu Apr 15 2010 Frederic Crozat <fcrozat@mandriva.com> 2.0.6-1mdv2010.1
+ Revision: 535091
- Release 2.0.6

* Wed Apr 14 2010 Frederic Crozat <fcrozat@mandriva.com> 2.0.5-1mdv2010.1
+ Revision: 534797
- Fix missing BR
- Release 2.0.5

* Fri Aug 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7.1-1mdv2010.0
+ Revision: 416386
- Update to new version 1.7.1

* Thu May 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.6.0-1mdv2010.0
+ Revision: 375709
- Update to new version 1.6.0

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.4.0-2mdv2009.1
+ Revision: 325686
- rebuild

* Mon Dec 08 2008 Thierry Vignaud <tv@mandriva.org> 1.4.0-1mdv2009.1
+ Revision: 311810
- new release

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2009.0
+ Revision: 282750
- rebuild

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-1mdv2009.0
+ Revision: 282732
- new release
- rebuild
- new release
- add download URL
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Thierry Vignaud <tv@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 80977
+ rebuild (emptylog)

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.9.0-2mdv2008.0
+ Revision: 80313
- fix x86_64 build
- new release
- sanitize spec file
- buildrequires python-devel
- new release
- Import ldtp



* Wed Aug 09 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.5.0-1mdv2007.0
- new release

* Tue Aug 08 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-1mdv2007.0
- initial release
