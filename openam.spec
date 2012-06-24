Summary:	Simple answering machine using the H.323 protocol
Summary(pl):	Prosty automat odpowiadaj�cy, u�ywaj�cy protoko�u H.323
Name:		openam
Version:	1.1.13
Release:	1
License:	MPL
Group:		Applications/Communications
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAM is a simple answering machine using the H.323 protocol. It is a
part of OpenH323 project.

%description -l pl
OpenAM to prosty automat odpowiadaj�cy, u�ywaj�cy protoko�u H.323.
Jest cz�ci� projektu OpenH323.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install obj_*/%{name}	$RPM_BUILD_ROOT%{_bindir}
install *.wav		$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt new_msg run_example
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
