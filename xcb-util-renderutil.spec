Name:		xcb-util-renderutil
Version:	0.3.8
Release:	5%{?dist}
Summary:	Convenience functions for the Render extension
Group:		System Environment/Libraries
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-renderutil module provides the following library:

  - renderutil: Convenience functions for the Render extension.


%package 	devel
Summary:	Development and header files for xcb-util-renderutil
Group:		System Environment/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-renderutil.


%prep
%setup -q


%build
%configure --with-pic --disable-static
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc README
%{_libdir}/*.so.*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.3.8-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.3.8-4
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.8-1
- New package.
