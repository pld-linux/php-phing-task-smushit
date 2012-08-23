%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Phing task to run Smush.it
Name:		php-phing-task-smushit
Version:	0.1
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/glensc/phing-task-smushit/tarball/master#/%{name}.tgz
# Source0-md5:	9cdbd0c9a2f3b5a8d5a6bf91577f84d1
URL:		https://github.com/glensc/phing-task-smushit
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php(core) >= %{php_min_version}
Requires:	php-smushit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		phingdir	%{php_data_dir}/phing
%define		tasksdir	%{phingdir}/tasks/ext

%define		_noautoreq	pear

%description
Phing task to run Smush.it

%prep
%setup -qc
mv */* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tasksdir}
cp -p *.php $RPM_BUILD_ROOT%{tasksdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%{tasksdir}/SmushitCompressorTask.php
