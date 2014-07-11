%define	_class	Net
%define	_subclass	Cyrus
%define	modname	%{_class}_%{_subclass}

Summary:	An API for the administration of Cyrus IMAP servers
Name:		php-pear-%{modname}
Version:	0.3.2
Release:	7
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_Cyrus/
Source0:	http://download.pear.php.net/package/Net_Cyrus-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
API for the administration of Cyrus IMAP servers. It can be used to
create,delete and modify users and it's properties (Quota and ACL)

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/tests
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

