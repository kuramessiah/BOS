Name:		b19-505-07	
Version:	1.0
Release:	1%{?dist}
Summary:	Программа студентки группы Б19-505

Group:		Testing
License:	GPL
URL:		https://github.com/kuramessiah/BOS
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	/bin/bash, /usr/bin/date

%description
A test package


%prep
%setup -q


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 b19-505-07 %{buildroot}%{_bindir}
sudo yum install gnuplot

%files
%{_bindir}/b19-505-07


%changelog
* Sun May 15 2022 <Иванова>
- Added %{_bindir}/b19-505-07
