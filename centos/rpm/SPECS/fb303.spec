%define thrift_name thrift

Name: 		fb303
Version: 	0.5.0
Release:	1%{?release_tag}	
License: 	MIT
Summary:    Multi-language RPC and serialization framework
Group:      Development/Libraries
URL: 		http://incubator.apache.org/thrift/
Source: 	%{thrift_name}-%{version}.tar.gz

BuildRoot: 	%{_tmppath}/%{thrift_name}-%{version}

%description
Facebook Baseline is a standard interface to monitoring, dynamic options and
configuration, uptime reports, activity, and more.

BuildRequires: thrift
Requires: thrift

%prep
%setup -q -n %{thrift_name}-%{version}

%build
cd contrib/fb303
./bootstrap.sh
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --with-thriftpath=%{_prefix} --disable-static 
%{__make}

%install
%{__rm} -rf %{buildroot}
cd contrib/fb303/cpp

make install DESTDIR=%{buildroot}
# Fix install path
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}/
rm -rf %{buildroot}/lib

%post
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Aug 16 2010 - jake farrell
- updated thrift version to 0.5.0
* Fri Jun 4 2010 - jake farrell
- Update thrift version to 0.4.0-dev r951482. 
* Thu May 17 2010 - jake farrell
- Initial rpm, fb303 from thrift version 0.2.0
