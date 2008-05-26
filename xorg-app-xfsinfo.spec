Summary:	xfsinfo application - X font server information utility
Summary(pl.UTF-8):	Aplikacja xfsinfo - narzędzie informacyjne dla serwera fontów X
Name:		xorg-app-xfsinfo
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfsinfo-%{version}.tar.bz2
# Source0-md5:	e6c0071f6d5436113982f4a575d3f94b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfsinfo is a utility for displaying information about an X font
server. It is used to examine the capabilities of a server, the
predefined values for various parameters used in communicating between
clients and the server, and the font catalogues and alternate servers
that are available.

%description -l pl.UTF-8
xfsinfo to narzędzie wyświetlające informacje o serwerze fontów X.
Służy do sprawdzania możliwości serwera, predefiniowanych wartości
różnych parametrów używanych przy komunikacji między klientami a
serwerem, katalogów fontów oraz innych dostępnych serwerów.

%prep
%setup -q -n xfsinfo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xfsinfo
%{_mandir}/man1/xfsinfo.1x*
