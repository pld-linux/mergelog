Summary:	Mergelog - a program which merges by date httpd log files
Summary(pl):	Mergelog - program ��cz�cy pliki log�w httpd wed�ug daty
Name:		mergelog
Version:	4.5
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d748039b14092315881fa329beeb6682
URL:		http://mergelog.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mergelog is a small and fast C program which merges by date httpd log
files in 'Common Log Format' from web servers behind round-robin DNS.
It has been designed to easily manage huge log files from highly
stressed servers. mergelog is distributed with zmergelog which
supports gzipped log files.

%description -l pl
mergelog to ma�y i szybki program w C ��cz�cy wed�ug daty pliki log�w
httpd w formacie "Common Log Format" z serwer�w WWW za DNS-em
ustawionym w round-robin. Zosta� zaprojektowany do �atwej obs�ugi
du�ych plik�w log�w z obci��onych serwer�w. mergelog jest
rozpowszechniany z programem zmergelog, kt�ry obs�uguje zgzipowane
pliki log�w.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*mergelog*
