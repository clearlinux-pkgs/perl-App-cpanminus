#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-App-cpanminus
Version  : 1.7044
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.7044.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.7044.tar.gz
Summary  : 'get, unpack, build and install modules from CPAN'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-App-cpanminus-bin = %{version}-%{release}
Requires: perl-App-cpanminus-license = %{version}-%{release}
Requires: perl-App-cpanminus-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
App::cpanminus - get, unpack, build and install modules from CPAN
SYNOPSIS
cpanm Module

%package bin
Summary: bin components for the perl-App-cpanminus package.
Group: Binaries
Requires: perl-App-cpanminus-license = %{version}-%{release}

%description bin
bin components for the perl-App-cpanminus package.


%package dev
Summary: dev components for the perl-App-cpanminus package.
Group: Development
Requires: perl-App-cpanminus-bin = %{version}-%{release}
Provides: perl-App-cpanminus-devel = %{version}-%{release}
Requires: perl-App-cpanminus = %{version}-%{release}

%description dev
dev components for the perl-App-cpanminus package.


%package license
Summary: license components for the perl-App-cpanminus package.
Group: Default

%description license
license components for the perl-App-cpanminus package.


%package man
Summary: man components for the perl-App-cpanminus package.
Group: Default

%description man
man components for the perl-App-cpanminus package.


%prep
%setup -q -n App-cpanminus-1.7044

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-App-cpanminus
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-App-cpanminus/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/App/cpanminus.pm
/usr/lib/perl5/vendor_perl/5.28.2/App/cpanminus/fatscript.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/cpanm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::cpanminus.3
/usr/share/man/man3/App::cpanminus::fatscript.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-App-cpanminus/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpanm.1
