Summary:	Simple answering machine using the H.323 protocol
Summary(pl.UTF-8):   Prosty automat odpowiadający, używający protokołu H.323
Name:		openam
Version:	1.13.5
%define fver	%(echo %{version} | tr . _)
Release:	5
License:	MPL 1.0
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	3e3bc94917c0b47b04474adac4ff7e4b
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.18.0
BuildRequires:	pwlib-devel >= 1.10.0
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAM is a simple answering machine using the H.323 protocol. It is a
part of OpenH323 project.

%description -l pl.UTF-8
OpenAM to prosty automat odpowiadający, używający protokołu H.323.
Jest częścią projektu OpenH323.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG} -fno-exceptions"

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
