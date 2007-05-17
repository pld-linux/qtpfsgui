Summary:	QtPFSGui - HDR Image compositor
Summary(pl.UTF-8):	QtPFSGui - narzędzie do składania obrazów HDR
Name:		qtpfsgui
Version:	1.8.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtpfsgui/%{name}-%{version}.tgz
# Source0-md5:	c72b621d8629532910103da0d165b177
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtPFSGui - HDR Image compositor.

%description -l pl.UTF-8
QtPFSGui - narzędzie do składania obrazów HDR.

%prep
%setup -q

%build
qt4-qmake -after target.path=/usr/bin 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
