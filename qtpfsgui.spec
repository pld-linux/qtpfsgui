#
Summary:	QtPFSGui - HDR Image compositor
Summary(pl.UTF-8):	QtPFSGui - narzędzie do składania obrazów HDR
Name:		qtpfsgui
Version:	1.8.12
Release:	0.3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.gz
# Source0-md5:	3a730548a681a20a43fffff68fdd46c3
Patch0:		%{name}-gcc43.patch
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	QtGui-devel
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtPFSGui - HDR Image compositor.

%description -l pl.UTF-8
QtPFSGui - narzędzie do składania obrazów HDR.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,Changelog,INSTALL,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/qtpfsgui.desktop
%{_iconsdir}/hicolor/48x48/apps/qtpfsgui.png
%{_datadir}/%{name}
