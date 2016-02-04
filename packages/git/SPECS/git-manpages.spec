Name: git-manpages
Version: 2.7.0
Release: 1%{?dist}
Summary: GIT man pages

License: GPL
Group: Development/Tools
URL: http://kernel.org/pub/software/scm/git/
Source0: https://git-core.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch: noarch

%description
GIT man pages.


%prep
%setup -q -c %{name}-%{version}


%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}
cp -r . $RPM_BUILD_ROOT%{_mandir}/


%files
%{_mandir}
