# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Crypt-IDEA
%define modver 1.10

Summary:	Perl interface to IDEA block cipher
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Crypt/Crypt-IDEA-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description 
This perl extension is an implementation of the IDEA block
cipher algorithm. The module implements the
Crypt::BlockCipher interface, which has the following
methods

blocksize =item keysize =item encrypt =item decrypt

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%check
make test

%install
%make_install

%files
%doc COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%doc %{_mandir}/man3/*
