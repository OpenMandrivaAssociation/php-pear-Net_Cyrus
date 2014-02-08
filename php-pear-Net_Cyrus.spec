%define		_class		Net
%define		_subclass	Cyrus
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.2
Release:	2
Summary:	An API for the administration of Cyrus IMAP servers
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Cyrus/
Source0:	http://download.pear.php.net/package/Net_Cyrus-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
API for the administration of Cyrus IMAP servers. It can be used to
create,delete and modify users and it's properties (Quota and ACL)

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/tests
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-15mdv2011.0
+ Revision: 667624
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-14mdv2011.0
+ Revision: 607121
- rebuild

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-13mdv2010.1
+ Revision: 468690
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.1-12mdv2010.0
+ Revision: 426657
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-11mdv2009.1
+ Revision: 321876
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-10mdv2009.0
+ Revision: 224754
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-9mdv2008.1
+ Revision: 178524
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdv2007.0
+ Revision: 82220
- Import php-pear-Net_Cyrus

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdk
- initial Mandriva package (PLD import)


