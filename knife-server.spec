#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	knife-server
Summary:	Chef Knife plugin to bootstrap Chef Servers
Name:		ruby-%{pkgname}
Version:	1.1.0
Release:	0.4
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	-
URL:		http://fnichol.github.com/knife-server
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-fakefs < 0.5
BuildRequires:	ruby-fakefs >= 0.4.0
BuildRequires:	ruby-knife-ec2 >= 0.5.12
BuildRequires:	ruby-knife-linode
BuildRequires:	ruby-rspec < 2.14
BuildRequires:	ruby-rspec >= 2.13.0
BuildRequires:	ruby-timecop < 1
BuildRequires:	ruby-timecop >= 0.3
%endif
Requires:	chef >= 0.10.10
#Requires:	ruby-fog < 2
#Requires:	ruby-fog >= 1.3
Requires:	ruby-net-ssh
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef Knife plugin to bootstrap Chef Servers.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb

%{ruby_vendorlibdir}/chef/knife/bootstrap/_common.sh
%{ruby_vendorlibdir}/chef/knife/bootstrap/_omnibus.sh
%{ruby_vendorlibdir}/chef/knife/bootstrap/_platform_and_version.sh
%{ruby_vendorlibdir}/chef/knife/bootstrap/_set_hostname.sh
%{ruby_vendorlibdir}/chef/knife/bootstrap/auto.sh
%dir %{ruby_vendorlibdir}/chef/knife/bootstrap/chef10
%{ruby_vendorlibdir}/chef/knife/bootstrap/chef10/debian.erb
%{ruby_vendorlibdir}/chef/knife/bootstrap/chef10/rhel.erb
%dir %{ruby_vendorlibdir}/chef/knife/bootstrap/chef11
%{ruby_vendorlibdir}/chef/knife/bootstrap/chef11/omnibus.erb
%{ruby_vendorlibdir}/chef/knife/bootstrap/chef11/rhel.erb
%{ruby_vendorlibdir}/chef/knife/server_backup.rb
%{ruby_vendorlibdir}/chef/knife/server_bootstrap_base.rb
%{ruby_vendorlibdir}/chef/knife/server_bootstrap_ec2.rb
%{ruby_vendorlibdir}/chef/knife/server_bootstrap_linode.rb
%{ruby_vendorlibdir}/chef/knife/server_bootstrap_standalone.rb
%{ruby_vendorlibdir}/chef/knife/server_restore.rb
%dir %{ruby_vendorlibdir}/knife
%dir %{ruby_vendorlibdir}/knife/server
%{ruby_vendorlibdir}/knife/server/credentials.rb
%{ruby_vendorlibdir}/knife/server/ec2_security_group.rb
%{ruby_vendorlibdir}/knife/server/ssh.rb
%{ruby_vendorlibdir}/knife/server/version.rb
