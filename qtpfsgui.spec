Summary:	QtPFSGui - HDR Image compositor
Summary(pl):	QtPFSGui - narzêdzie do sk³adania obrazów HDR
Name:		qtpfsgui
Version:	1.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.gz
# Source0-md5:	503202f36ec312b67db379edb1f1a7f7
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtPFSGui - HDR Image compositor.

%description -l pl
QtPFSGui - narzêdzie do sk³adania obrazów HDR.

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
