Summary:	Mergelog is a program which merges by date httpd log files
Name:		mergelog
Version:	4.5
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d748039b14092315881fa329beeb6682
URL:		http://mergelog.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mergelog is a small and fast C program which merges by date httpd log
files in 'Common Log Format' from web servers behind round-robin DNS.
It has been designed to easily manage huge log files from highly
stressed servers. mergelog is distributed with zmergelog which
supports gzipped log files

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
