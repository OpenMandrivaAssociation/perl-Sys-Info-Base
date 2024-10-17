%define upstream_name    Sys-Info-Base
%define upstream_version 0.78

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(TARGET_CLASS\\)'
%else
%define _requires_exceptions perl(TARGET_CLASS)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Base classes for Sys::Info
License:    GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
Perl base classes for Sys::Info.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.780.0-1mdv2011.0
+ Revision: 662466
- update to new version 0.78

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-2mdv2011.0
+ Revision: 493594
- adding some requires exceptions

* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.1
+ Revision: 491170
- update to 0.73

* Fri Jan 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 484721
- SILET fix it
- import perl-Sys-Info-Base


