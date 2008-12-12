#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Authentication-Store-DBIx-Class
Summary:	Catalyst::Authentication::Store::DBIx::Class - A storage class for Catalyst Authentication using DBIx::Class
#Summary(pl.UTF-8):	
Name:		perl-Catalyst-Authentication-Store-DBIx-Class
Version:	0.1082
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c057bed16d46cd5ac73fdbd0d22b1643
URL:		http://search.cpan.org/dist/Catalyst-Authentication-Store-DBIx-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Catalyst-Model-DBIC-Schema >= 0.18
BuildRequires:	perl-Catalyst-Plugin-Authentication >= 0.10008
BuildRequires:	perl-DBIx-Class
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Catalyst::Authentication::Store::DBIx::Class class provides 
access to authentication information stored in a database via DBIx::Class.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL --skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Catalyst/Authentication/Store/DBIx
%{perl_vendorlib}/Catalyst/Authentication/Store/DBIx/*.pm
%{perl_vendorlib}/Catalyst/Authentication/Store/DBIx/Class
%{perl_vendorlib}/Catalyst/Authentication/Realm/*
%{_mandir}/man3/*
