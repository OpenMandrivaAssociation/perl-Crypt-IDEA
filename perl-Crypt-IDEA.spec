%define upstream_name	 Crypt-IDEA
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl interface to IDEA block cipher
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

%description 
This perl extension is an implementation of the IDEA block
cipher algorithm. The module implements the
Crypt::BlockCipher interface, which has the following
methods

blocksize =item keysize =item encrypt =item decrypt

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-5mdv2012.0
+ Revision: 765127
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-4
+ Revision: 763630
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-3
+ Revision: 676568
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 555714
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 406926
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.08-5mdv2009.0
+ Revision: 256267
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2008.1
+ Revision: 152034
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 1.08-2mdv2008.0
+ Revision: 19110
- rebuild


* Thu Apr 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdk
- New release 1.08
- better source URL
- correct optimisations

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdk
- New release 1.07

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdk
- New release 1.06
- spec cleanup
- better source URL, URL
- fix directory ownership
- %%mkrel

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1.02-2mdk
- Rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.02-1mdk
- New package

