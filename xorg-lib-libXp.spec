Summary:	DtPrint extension library
Summary(pl):	Biblioteka rozszerzenia DtPrint
Name:		xorg-lib-libXp
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXp-%{version}.tar.bz2
# Source0-md5:	8455bf5abe4496a8fb4a1c8d11d5cbf9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
Obsoletes:	libXp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DtPrint extension library.

%description -l pl
Biblioteka rozszerzenia DtPrint.

%package devel
Summary:	Header files libXp development
Summary(pl):	Pliki nagłówkowe do biblioteki libXp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-printproto-devel
Obsoletes:	libXp-devel

%description devel
DtPrint extension library.

This package contains the header files needed to develop programs that
use these libXp.

%description devel -l pl
Biblioteka rozszerzenia DtPrint.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXp.

%package static
Summary:	Static libXp library
Summary(pl):	Biblioteka statyczna libXp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXp-static

%description static
DtPrint extension library.

This package contains the static libXp library.

%description static -l pl
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
	libmandir=%{_mandir}/man3 \
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
