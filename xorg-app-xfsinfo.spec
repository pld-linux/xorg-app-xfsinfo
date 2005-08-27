# $Rev: 3389 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xfsinfo application
Summary(pl):	Aplikacja xfsinfo
Name:		xorg-app-xfsinfo
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xfsinfo-%{version}.tar.bz2
# Source0-md5:	8514f490f6d91ab4813c2aaee3e7b19e
Patch0:		xfsinfo-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xfsinfo-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xfsinfo application.

%description -l pl
Aplikacja xfsinfo.


%prep
%setup -q -n xfsinfo-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
