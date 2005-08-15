
#
Summary:	DtPrint extension library
Summary(pl):	Biblioteka rozszerzenia DtPrint
Name:		xorg-lib-libXp
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXp-%{version}.tar.bz2
# Source0-md5:	a8c73c15ae3a96ab2595762df1edea5f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXp-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
DtPrint extension library.

%description -l pl
Biblioteka rozszerzenia DtPrint.


%package devel
Summary:	Header files libXp development
Summary(pl):	Pliki nagłówkowe do biblioteki libXp
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXp = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-printproto-devel

%description devel
DtPrint extension library.

This package contains the header files needed to develop programs that
use these libXp.

%description devel -l pl
Biblioteka rozszerzenia DtPrint.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXp.


%package static
Summary:	Static libXp libraries
Summary(pl):	Biblioteki statyczne libXp
Group:		Development/Libraries
Requires:	xorg-lib-libXp-devel = %{version}-%{release}

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
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXp.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXp.la
%attr(755,root,wheel) %{_libdir}/libXp.so
%{_pkgconfigdir}/xp.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXp.a
