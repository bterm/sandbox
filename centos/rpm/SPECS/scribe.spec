Name: 		scribe
Version: 	2.2
Release:	5%{?release_tag}	
License: 	Apache v2
Summary:    A server for aggregating log data streamed in real time
Group:      Development/Libraries
URL: 		http://github.com/facebook/scribe
Source: 	%{name}-%{version}.tar.gz
Patch0:		%{name}.thrift-0.5.0.patch

BuildRoot: 	%{_tmppath}/%{name}

%description
Scribe is a server for aggregating log data streamed in real time from a large
number of servers. It is designed to be scalable, extensible without
client-side modification, and robust to failure of the network or any specific
machine.

%define python_prefix /usr
%define _requires_exceptions %{python_prefix}/bin/python

BuildRequires: thrift
BuildRequires: fb303
Requires: boost
Requires: libevent
Requires: thrift
Requires: fb303

%prep
%setup -q -n %{name} -b 1
%patch0 -p1

%build
./bootstrap.sh LDFLAGS=-L%{_libdir} --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static --with-thriftpath=%{_prefix} --with-fb303path=%{_prefix}  --with-boost==%{_prefix} --with-boost-system=boost_system --with-boost-filesystem=boost_filesystem
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 ./src/scribed %{buildroot}%{_bindir}/scribed
%{__install} -D -m 755 ./examples/scribe_cat %{buildroot}%{_bindir}/scribe_cat
%{__install} -D -m 755 ./examples/scribe_ctrl %{buildroot}%{_bindir}/scribe_ctrl
%{__install} -D -m 755 ./src/libscribe.so %{buildroot}%{_libdir}/libscribe.so
%{__install} -D -m 755 ./if/scribe.thrift %{buildroot}%{_datadir}/if/scribe.thrift
%{__install} -D -m 755 ./scripts/scribe-client %{buildroot}%{_sysconfdir}/rc.d/init.d/scribe-client
%{__install} -D -m 755 ./scripts/scribe-server %{buildroot}%{_sysconfdir}/rc.d/init.d/scribe-server


# replace /usr/local/bin/thrift in scribe.thrift with actual location of thrift
sed -i 's/\/usr\/local\/bin\/thrift/\/usr\/bin\/thrift/g' %{buildroot}%{_datadir}/if/scribe.thrift

%post
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Tue Aug 17 2010 - jake farrell
- recompiling against thrift 0.5.0
* Fri Jun 4 2010 - jake farrell
- Update scribe version to 2.2. 
* Thu May 17 2010 - jake farrell
- Initial rpm, scribe version 2.1. Does not build with scribe libs (py, java, php, ..) will have to be built as needed
