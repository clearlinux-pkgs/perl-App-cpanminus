#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-App-cpanminus
Version  : 1.7047
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.7047.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.7047.tar.gz
Summary  : 'get, unpack, build and install modules from CPAN'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-App-cpanminus-bin = %{version}-%{release}
Requires: perl-App-cpanminus-license = %{version}-%{release}
Requires: perl-App-cpanminus-man = %{version}-%{release}
Requires: perl-App-cpanminus-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package perl
Summary: perl components for the perl-App-cpanminus package.
Group: Default
Requires: perl-App-cpanminus = %{version}-%{release}

%description perl
perl components for the perl-App-cpanminus package.


%prep
%setup -q -n App-cpanminus-1.7047
cd %{_builddir}/App-cpanminus-1.7047
pushd ..
cp -a App-cpanminus-1.7047 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-App-cpanminus
cp %{_builddir}/App-cpanminus-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-App-cpanminus/417bb11ff333b09a84459664db9c4ea05b039ba7 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cpanm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::cpanminus.3
/usr/share/man/man3/App::cpanminus::fatscript.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-App-cpanminus/417bb11ff333b09a84459664db9c4ea05b039ba7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpanm.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
