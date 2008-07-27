Summary:	DtPrint extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia DtPrint
Name:		xorg-lib-libXp
Version:	1.0.0
Release:	4
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libXp-%{version}.tar.bz2
# Source0-md5:	0f4ac39108c1ae8c443cdfac259b58fa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DtPrint extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia DtPrint.

%package devel
Summary:	Header files for libXp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-printproto-devel
Obsoletes:	libXp-devel

%description devel
DtPrint extension library.

This package contains the header files needed to develop programs that
use libXp.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia DtPrint.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXp.

%package static
Summary:	Static libXp library
Summary(pl.UTF-8):	Biblioteka statyczna libXp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXp-static

%description static
DtPrint extension library.

This package contains the static libXp library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia DtPrint.

Pakiet zawiera statyczną bibliotekę libXp.

%prep
%setup -q -n libXp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXp.so
%{_libdir}/libXp.la
%{_pkgconfigdir}/xp.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXp.a
