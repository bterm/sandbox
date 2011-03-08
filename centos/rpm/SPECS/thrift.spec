Name: 		thrift
Version: 	0.5.0
Release:	1%{?release_tag}	
License: 	MIT
Summary:    Multi-language RPC and serialization framework
Group:      Development/Libraries
URL: 		http://incubator.apache.org/thrift/
Source: 	%{name}-%{version}.tar.gz


BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Thrift is a software framework for scalable cross-language services
development. It combines a powerful software stack with a code generation
engine to build services that work efficiently and seamlessly between C++,
Java, C#, Python, Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang,
Objective Caml, and Haskell.

%package devel
Summary: Development tools for the %{name}-%{version}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains client libraries for %{name}. If you like to develop 
programs using %{name}, you will need to install %{name}-devel.

%define python_prefix /usr/
%define java_prefix /usr/java/lib

BuildRequires: boost
BuildRequires: libevent

%prep
%setup -q -n %{name}-%{version}
# %patch -p1

%build
#./bootstrap.sh
PATH=%{python_prefix}/bin:$PATH %configure PY_PREFIX=%{python_prefix} JAVA_PREFIX=%{java_prefix} --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --disable-static --without-ruby --without-erlang --without-haskell --without-perl --without-csharp --without-java --without-php --without-python 
%{__make}

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

%post
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
#%exclude %{_datadir}/doc/*
#%exclude %{python_prefix}/lib/python*
#%exclude %{java_prefix}/*

%files devel
%defattr(-, root, root, 0755)
#%{python_prefix}/lib/python*
#%{java_prefix}/*
#%{_datadir}/doc/*


%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Aug 16 2010 - jake farrell
- updated thrift version to 0.5.0
* Fri Jun 4 2010 - jake farrell
- Update thrift version to 0.4.0-dev r951482. 
- Does not build with thrift libs (py, java, php, ..) will have to be built as needed
* Thu May 17 2010 - jake farrell
- Initial rpm, thrift version 0.2.0. Does not build with thrift libs (py, java, php, ..) will have to be built as needed
