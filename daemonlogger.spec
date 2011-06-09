%define name daemonlogger
%define version 1.2.1

Name: %{name}
Summary: Simple packet logging daemon
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: Monitoring
Source: http://www.snort.org/users/roesch/code/%{name}-%{version}.tar.gz
URL:	http://www.snort.org/users/roesch/Site/Daemonlogger/Daemonlogger.html
BuildRequires: libpcap1 libdnet libdnet-devel
Requires: libpcap1 libdnet
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
This is a libpcap-based program.  It has two runtime modes:

1) It sniffs packets and spools them straight to the disk and can daemonize 
itself for background packet logging.  By default the file rolls over when 
1 GB of data is logged.

2) It sniffs packets and rewrites them to a second interface, essentially 
acting as a soft tap.  It can also do this in daemon mode.

These two runtime modes are mutually exclusive, if the program is placed in
tap mode (using the -I switch) then logging to disk is disabled.

%prep
%setup -q

%build 
%configure
%make

%install
rm -rf %{buildroot}
%{__install} -D -m 0700 %{name} %{buildroot}%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING
%attr(0700,root,root) %{_sbindir}/%{name}
