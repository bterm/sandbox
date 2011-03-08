Name: 		boost
Version: 	1.42.0
Release:	1%{?release_tag}	
License: 	Boost
Summary:    The free peer-reviewed portable C++ source libraries
Group:      Development/Libraries
URL: 		http://www.boost.org/
Source0: 	boost-%{version}.tar.gz

BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%prep
%setup -q -n %{name}-%{version}

%build
./bootstrap.sh --prefix=%{_prefix} --exec-prefix=%{_prefix} --libdir=%{_libdir}
./bjam

%install
%{__rm} -rf %{buildroot}
./bjam --prefix=%{buildroot} --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} install

%post
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/*
%{_includedir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Apr 1 2010 - jake farrell
- Initial rpm, boost version 1.42.0
