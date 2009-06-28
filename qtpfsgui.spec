#
Summary:	QtPFSGui - HDR Image compositor
Summary(pl.UTF-8):	QtPFSGui - narzędzie do składania obrazów HDR
Name:		qtpfsgui
Version:	1.9.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.gz
# Source0-md5:	5a6421391e373c912e4a793e131151c8
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	QtGui-devel
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt-linguist
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtPFSGui - HDR Image compositor.

%description -l pl.UTF-8
QtPFSGui - narzędzie do składania obrazów HDR.

%prep
%setup -q

%build
qmake-qt4 PREFIX=%{_prefix}
%{__make}
lrelease project.pro

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,Changelog,INSTALL,LICENSE,README}

cp -f i18n/lang_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/i18n

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/32x32/apps/qtpfsgui.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/html
%dir %{_datadir}/%{name}/i18n
%lang(cs) %{_datadir}/%{name}/i18n/lang_cs.qm
%lang(de) %{_datadir}/%{name}/i18n/lang_de.qm
%lang(es) %{_datadir}/%{name}/i18n/lang_es.qm
%lang(fr) %{_datadir}/%{name}/i18n/lang_fr.qm
%lang(hu) %{_datadir}/%{name}/i18n/lang_hu.qm
%lang(id) %{_datadir}/%{name}/i18n/lang_id.qm
%lang(it) %{_datadir}/%{name}/i18n/lang_it.qm
%lang(pl) %{_datadir}/%{name}/i18n/lang_pl.qm
%lang(ru) %{_datadir}/%{name}/i18n/lang_ru.qm
%lang(tr) %{_datadir}/%{name}/i18n/lang_tr.qm
