#
# Conditinal build:
%bcond_without	apidocs		# API documentation
%bcond_without	caja		# Caja extension
%bcond_without	gconf		# GConf subsystem (deprecated)
%bcond_without	nautilus	# Nautilus extension
%bcond_without	nemo		# Nemo extension

Summary:	A file-manager extension which offers user configurable context menu actions
Summary(pl.UTF-8):	Rozszerzenie zarządców plików dodające własne polecenia w menu kontekstowym
Name:		filemanager-actions
Version:	3.4
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/filemanager-actions/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	5748c9228705645ea67f273c12439955
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-no-nautilus.patch
Patch2:		%{name}-gtkdoc.patch
URL:		https://gitlab.gnome.org/Archive/filemanager-actions
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.8.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_nautilus:BuildRequires:	caja-devel >= 1.16.0}
%{?with_nemo:BuildRequires:	cinnamon-nemo-devel >= 1.8}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.1
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.4.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.16}
BuildRequires:	intltool >= 0.50.2
BuildRequires:	libgtop-devel >= 1:2.28.4
BuildRequires:	libtool
BuildRequires:	libuuid-devel >= 1.6.2
BuildRequires:	libxml2-devel >= 1:2.7.8
%{?with_nautilus:BuildRequires:	nautilus3-devel >= 3.4.1}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
%{?with_gconf:Requires:	GConf2 >= 2.8.0}
Requires:	glib2 >= 1:2.32.1
Requires:	gtk+3 >= 3.4.1
Requires:	hicolor-icon-theme
Requires:	libgtop >= 1:2.28.4
Requires:	libxml2 >= 1:2.7.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-actions is an extension for Nautilus file manager which
allows the user to add arbitrary program to be launched through the
Nautilus file manager popup menu of selected files.

%description -l pl.UTF-8
Rozszerzenie pozwalające na skonfigurowanie programu uruchamianego na
pliku wybranym w Nautilusie.

%package devel
Summary:	Header files for FileManager-Actions extension interface
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu rozszerzeń FileManager-Actions
Group:		X11/Development/Libraries
%{?with_gconf:Requires:	GConf2-devel >= 2.8.0}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.32.1

%description devel
Header files for FileManager-Actions extension interface.

%description devel -l pl.UTF-8
Pliki nagłówkowe interfejsu rozszerzeń FileManager-Actions

%package apidocs
Summary:	FileManager-Actions extension API documentation
Summary(pl.UTF-8):	Dokumentacja API rozszerzeń FileManager-Actions
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
FileManager-Actions extension API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API rozszerzeń FileManager-Actions.

%package -n caja-actions
Summary:	Caja extension which adds customized command in Caja menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu zarządcy plików Caja
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	caja >= 1.16.0

%description -n caja-actions
Caja-actions is an extension for Caja file manager which allows the
user to add arbitrary program to be launched through the Caja file
manager popup menu of selected files.

%description -n caja-actions -l pl.UTF-8
Rozszerzenie zarządcy plików Caja pozwalające dodać możliwość
uruchamiania dowolnego programu z poziomu menu kontekstowego zarządcy
dla wybranych plików.

%package -n nautilus-actions
Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus3 >= 3.4.1

%description -n nautilus-actions
Nautilus-actions is an extension for Nautilus file manager which
allows the user to add arbitrary program to be launched through the
Nautilus file manager popup menu of selected files.

%description -n nautilus-actions -l pl.UTF-8
Rozszerzenie Nautilusa pozwalające dodać możliwość uruchamiania
dowolnego programu z poziomu menu kontekstowego zarządcy dla wybranych
plików.

%package -n cinnamon-nemo-actions
Summary:	Nemo extension which adds customized command in Nautilus menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu Nemo
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	cinnamon-nemo >= 1.8

%description -n cinnamon-nemo-actions
Nemo-actions is an extension for Nemo file manager which allows the
user to add arbitrary program to be launched through the Nemo file
manager popup menu of selected files.

%description -n cinnamon-nemo-actions -l pl.UTF-8
Rozszerzenie zarządcy plików Nemo pozwalające dodać możliwość
uruchamiania dowolnego programu z poziomu menu kontekstowego zarządcy
dla wybranych plików.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gconf:--enable-gconf} \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--disable-schemas-install \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_caja:--without-caja} \
	%{!?with_nautilus:--without-nautilus} \
	%{!?with_nemo:--without-nemo}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs-installed
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} docs-installed
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/filemanager-actions/*.la
%if %{with caja}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la
%endif
%if %{with nautilus}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%endif
%if %{with nemo}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nemo/extensions-3.0/*.la
%endif

%{!?with_apidocs:%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

# filemanager actions gettext domain, fma-config-tool help, fma-config-tool omf
%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README README-GCONF TODO docs-installed/html
%attr(755,root,root) %{_bindir}/fma-config-tool
%dir %{_libdir}/filemanager-actions
%attr(755,root,root) %{_libdir}/filemanager-actions/libfma-core.so
%attr(755,root,root) %{_libdir}/filemanager-actions/libfma-io-desktop.so
%if %{with gconf}
%attr(755,root,root) %{_libdir}/filemanager-actions/libfma-io-gconf.so
%endif
%attr(755,root,root) %{_libdir}/filemanager-actions/libfma-io-xml.so
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/filemanager-actions
%endif
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-new
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-print
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-print-schemas
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-run
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-set-conf
%if %{with gconf}
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-delete-xmltree
%attr(755,root,root) %{_libexecdir}/filemanager-actions/fma-gconf2key.sh
%endif
%{_datadir}/filemanager-actions
%{_datadir}/fma-config-tool
%{_desktopdir}/fma-config-tool.desktop
%{_iconsdir}/hicolor/*x*/apps/filemanager-actions.png
%{_iconsdir}/hicolor/scalable/apps/filemanager-actions.svg

%files devel
%defattr(644,root,root,755)
%doc src/api/README
%{_includedir}/filemanager-actions

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/filemanager-actions-3
%endif

%if %{with caja}
%files -n caja-actions
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libfma-caja-menu.so
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libfma-caja-tracker.so
%endif

%if %{with nautilus}
%files -n nautilus-actions
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libfma-nautilus-menu.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libfma-nautilus-tracker.so
%endif

%if %{with nemo}
%files -n cinnamon-nemo-actions
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libfma-nemo-menu.so
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libfma-nemo-tracker.so
%endif
