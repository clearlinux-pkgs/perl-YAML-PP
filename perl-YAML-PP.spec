#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML-PP
Version  : 0.033
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-PP-0.033.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-PP-0.033.tar.gz
Summary  : 'YAML 1.2 Processor'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-PP-bin = %{version}-%{release}
Requires: perl-YAML-PP-license = %{version}-%{release}
Requires: perl-YAML-PP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Warn)

%description
# Perl module YAML::PP
YAML::PP is a modular YAML processor for YAML 1.2.
Additionally to loading and dumping it provides a parser and emitter. The
parsing events are compatible to the [YAML Test
Suite](https://github.com/yaml/yaml-test-suite) and other libraries like
[libyaml](https://github.com/yaml/libyaml).

%package bin
Summary: bin components for the perl-YAML-PP package.
Group: Binaries
Requires: perl-YAML-PP-license = %{version}-%{release}

%description bin
bin components for the perl-YAML-PP package.


%package dev
Summary: dev components for the perl-YAML-PP package.
Group: Development
Requires: perl-YAML-PP-bin = %{version}-%{release}
Provides: perl-YAML-PP-devel = %{version}-%{release}
Requires: perl-YAML-PP = %{version}-%{release}

%description dev
dev components for the perl-YAML-PP package.


%package license
Summary: license components for the perl-YAML-PP package.
Group: Default

%description license
license components for the perl-YAML-PP package.


%package perl
Summary: perl components for the perl-YAML-PP package.
Group: Default
Requires: perl-YAML-PP = %{version}-%{release}

%description perl
perl components for the perl-YAML-PP package.


%prep
%setup -q -n YAML-PP-0.033
cd %{_builddir}/YAML-PP-0.033

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-YAML-PP
cp %{_builddir}/YAML-PP-0.033/LICENSE %{buildroot}/usr/share/package-licenses/perl-YAML-PP/ce5601188e3eaef45d9491ce50709337e05115ef
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

%files bin
%defattr(-,root,root,-)
/usr/bin/yamlpp-events
/usr/bin/yamlpp-highlight
/usr/bin/yamlpp-load
/usr/bin/yamlpp-load-dump
/usr/bin/yamlpp-parse-emit

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/YAML::PP.3
/usr/share/man/man3/YAML::PP::Common.3
/usr/share/man/man3/YAML::PP::Constructor.3
/usr/share/man/man3/YAML::PP::Emitter.3
/usr/share/man/man3/YAML::PP::Grammar.3
/usr/share/man/man3/YAML::PP::Highlight.3
/usr/share/man/man3/YAML::PP::Perl.3
/usr/share/man/man3/YAML::PP::Schema.3
/usr/share/man/man3/YAML::PP::Schema::Binary.3
/usr/share/man/man3/YAML::PP::Schema::Core.3
/usr/share/man/man3/YAML::PP::Schema::Failsafe.3
/usr/share/man/man3/YAML::PP::Schema::Include.3
/usr/share/man/man3/YAML::PP::Schema::JSON.3
/usr/share/man/man3/YAML::PP::Schema::Merge.3
/usr/share/man/man3/YAML::PP::Schema::Perl.3
/usr/share/man/man3/YAML::PP::Schema::Tie::IxHash.3
/usr/share/man/man3/YAML::PP::Schema::YAML1_1.3
/usr/share/man/man3/YAML::PP::Type::MergeKey.3
/usr/share/man/man3/YAML::PP::Writer.3
/usr/share/man/man3/YAML::PP::Writer::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-YAML-PP/ce5601188e3eaef45d9491ce50709337e05115ef

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
