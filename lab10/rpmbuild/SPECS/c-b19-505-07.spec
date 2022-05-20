Name:		c-b19-505-07		
Version:	1.0
Release:	1%{?dist}
Summary:	Программа студентки Ивановой (да, забыла в прошлом файле) группы Б19-505

Group:		Testing
License:	GPL
URL:		https://github.com/kuramessiah/BOS
Source:		%{name}-%{version}.tar.gz

BuildRequires:	gcc	
Requires:	gcc

%description
A test package


%prep
%setup -q


%build
gcc -O2 -o c-b19-505-07 c-b19-505-07.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-505-07 %{buildroot}%{_bindir}

%files
%{_bindir}/c-b19-505-07

%changelog
* Sun May 15 2022 <Иванова>
- Added %{_bindir}/c-b19-505-07
