Summary:	Simple answering machine using the H.323 protocol
Summary(pl):	Prosty automat odpowiadający, używający protokołu H.323
Name:		openam
Version:	1.13.4
%define fver	%(echo %{version} | tr . _)
Release:	2
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	6eba766ce41c5bc4dbf25a0fdb5afd09
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.13.4-3
BuildRequires:	pwlib-devel >= 1.6.5-3
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAM is a simple answering machine using the H.323 protocol. It is a
part of OpenH323 project.

%description -l pl
OpenAM to prosty automat odpowiadający, używający protokołu H.323.
Jest częścią projektu OpenH323.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG} -fno-rtti -fno-exceptions"

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
