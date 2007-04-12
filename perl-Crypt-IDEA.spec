%define module	Crypt-IDEA
%define name	perl-%{module}
%define version 1.08
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Perl interface to IDEA block cipher
License:	GPL or Artistic
Group:          Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
This perl extension is an implementation of the IDEA block
cipher algorithm. The module implements the
Crypt::BlockCipher interface, which has the following
methods

blocksize =item keysize =item encrypt =item decrypt

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/*/*

