%define modname	Crypt-IDEA
%define modver	1.08

Summary:	Perl interface to IDEA block cipher
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel

%description 
This perl extension is an implementation of the IDEA block
cipher algorithm. The module implements the
Crypt::BlockCipher interface, which has the following
methods

blocksize =item keysize =item encrypt =item decrypt

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3/*

