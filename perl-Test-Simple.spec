%{?scl:%scl_package perl-Test-Simple}

Name:           %{?scl_prefix}perl-Test-Simple
Summary:        Basic utilities for writing tests
Version:        1.302040
Release:        2%{?dist}
# CC0: lib/ok.pm
# Public Domain: lib/Test/Tutorial.pod
# GPL+ or Artistic: the rest of the distribution
License:        (GPL+ or Artistic) and CC0 and Public Domain
URL:            http://search.cpan.org/dist/Test-Simple
Source0:        http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.75
# Module Runtime
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util) >= 1.13
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(Term::ANSIColor)
BuildRequires:  %{?scl_prefix}perl(threads::shared)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(IO::Pipe)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(PerlIO)
BuildRequires:  %{?scl_prefix}perl(threads)
# Optional Tests
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.120920
BuildRequires:  %{?scl_prefix}perl(IPC::SysV)
BuildRequires:  %{?scl_prefix}perl(Module::Metadata)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Test::Harness) >= 2.03
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Data::Dumper)
Requires:       %{?scl_prefix}perl(Term::ANSIColor)
Requires:       %{?scl_prefix}perl(threads::shared)

# Test-Tester and Test-use-ok integrated at version 1.001010
# Test2 integrated at 1.302014
Obsoletes:      %{?scl_prefix}perl-Test-Tester < 0.109-7
Provides:       %{?scl_prefix}perl-Test-Tester = %{version}-1%{?dist}
Obsoletes:      %{?scl_prefix}perl-Test-use-ok < 0.11-7
Provides:       %{?scl_prefix}perl-Test-use-ok = %{version}-1%{?dist}
Obsoletes:      %{?scl_prefix}perl-Test2 < %{version}-%{release}
Provides:       %{?scl_prefix}perl-Test2 = %{version}-%{release}

%{?perl_default_filter}

%description
This package provides the bulk of the core testing facilities. For more
information, see perldoc for Test::Simple, Test::More, etc.

This package is the CPAN component of the dual-lifed core package Test-Simple.

%prep
%setup -q -n Test-Simple-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test AUTHOR_TESTING=1%{?scl:'}

%files
%doc LICENSE
%doc Changes README examples/ t/
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/ok.pm
%{perl_vendorlib}/Test/Builder.pm
%{perl_vendorlib}/Test/Builder/
%{perl_vendorlib}/Test/More.pm
%{perl_vendorlib}/Test/Simple.pm
%{perl_vendorlib}/Test/Tester.pm
%{perl_vendorlib}/Test/Tester/
%doc %{perl_vendorlib}/Test/Tutorial.pod
%{perl_vendorlib}/Test/use/
%{perl_vendorlib}/Test2.pm
%{perl_vendorlib}/Test2/
%{_mandir}/man3/ok.3*
%{_mandir}/man3/Test::Builder.3*
%{_mandir}/man3/Test::Builder::Formatter.3*
%{_mandir}/man3/Test::Builder::IO::Scalar.3*
%{_mandir}/man3/Test::Builder::Module.3*
%{_mandir}/man3/Test::Builder::Tester.3*
%{_mandir}/man3/Test::Builder::Tester::Color.3*
%{_mandir}/man3/Test::Builder::TodoDiag.3*
%{_mandir}/man3/Test::More.3*
%{_mandir}/man3/Test::Simple.3*
%{_mandir}/man3/Test::Tester.3*
%{_mandir}/man3/Test::Tester::Capture.3*
%{_mandir}/man3/Test::Tester::CaptureRunner.3*
%{_mandir}/man3/Test::Tutorial.3*
%{_mandir}/man3/Test::use::ok.3*
%{_mandir}/man3/Test2.3*
%{_mandir}/man3/Test2::API.3*
%{_mandir}/man3/Test2::API::Breakage.3*
%{_mandir}/man3/Test2::API::Context.3*
%{_mandir}/man3/Test2::API::Instance.3*
%{_mandir}/man3/Test2::API::Stack.3*
%{_mandir}/man3/Test2::Event.3*
%{_mandir}/man3/Test2::Event::Bail.3*
%{_mandir}/man3/Test2::Event::Diag.3*
%{_mandir}/man3/Test2::Event::Exception.3*
%{_mandir}/man3/Test2::Event::Generic.3*
%{_mandir}/man3/Test2::Event::Info.3*
%{_mandir}/man3/Test2::Event::Note.3*
%{_mandir}/man3/Test2::Event::Ok.3*
%{_mandir}/man3/Test2::Event::Plan.3*
%{_mandir}/man3/Test2::Event::Skip.3*
%{_mandir}/man3/Test2::Event::Subtest.3*
%{_mandir}/man3/Test2::Event::Waiting.3*
%{_mandir}/man3/Test2::Formatter.3*
%{_mandir}/man3/Test2::Formatter::TAP.3*
%{_mandir}/man3/Test2::Hub.3*
%{_mandir}/man3/Test2::Hub::Interceptor.3*
%{_mandir}/man3/Test2::Hub::Interceptor::Terminator.3*
%{_mandir}/man3/Test2::Hub::Subtest.3*
%{_mandir}/man3/Test2::IPC.3*
%{_mandir}/man3/Test2::IPC::Driver.3*
%{_mandir}/man3/Test2::IPC::Driver::Files.3*
%{_mandir}/man3/Test2::Transition.3*
%{_mandir}/man3/Test2::Util.3*
%{_mandir}/man3/Test2::Util::ExternalMeta.3*
%{_mandir}/man3/Test2::Util::HashBase.3*
%{_mandir}/man3/Test2::Util::Trace.3*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.302040-2
- SCL

* Sun Jul 10 2016 Paul Howarth <paul@city-fan.org> - 1.302040-1
- Update to 1.302040
  - Fix broken MANIFEST.SKIP entries (#689)
  - Add Info event for better diagnostics

* Mon Jul  4 2016 Paul Howarth <paul@city-fan.org> - 1.302037-1
- Update to 1.302037
  - Restore PerlIO layer cloning on STDERR and STDOUT
- Bump obsoletes/provides versions for perl-Test2 to maintain upgrade path from
  packages in third-party repositories

* Tue Jun 28 2016 Paul Howarth <paul@city-fan.org> - 1.302035-1
- Update to 1.302035
  - Fix some breakage info
  - POD fixes

* Fri Jun 24 2016 Paul Howarth <paul@city-fan.org> - 1.302033-1
- Update to 1.302033
  - Fix nested TODO handling of diags (#684)

* Wed Jun 22 2016 Paul Howarth <paul@city-fan.org> - 1.302031-1
- Update to 1.302031
  - Remove Carp from dependency list (#682)

* Sun Jun 19 2016 Paul Howarth <paul@city-fan.org> - 1.302030-1
- Update to 1.302030
  - Use pre_filter instead of filter for TODO in Test::Builder (fix #683)
  - Fix typos in transitions doc (#681)
  - Add 'inherit_trace' param to run_subtest
  - Properly skip thread test when threads are broken

* Tue Jun 14 2016 Paul Howarth <paul@city-fan.org> - 1.302026-1
- Update to 1.302026
  - Do not fail if Test2::API::Breakage cannot load (rare 5.10.0 issue)
  - Potential fix for t/Legacy/Regression/637.t
  - Make t/Legacy/Regression/637.t AUTHOR_TESTING for now
  - Add Generic event type
  - Make sure enabling culling/shm sets pid and tid (fix #679)

* Sun May 29 2016 Paul Howarth <paul@city-fan.org> - 1.302022-1
- Update to 1.302022
  - Many micro-optimizations
  - Spelling fixes and tests
  - Fix leaky File.t file so that tmp doesn't fill up
  - Move some modules out of the known broken list in xt tests
  - Add Test2-based tools to downstream testing
  - Change when PID/TID are stashed (for forkprove)
  - VMS fixes for Files.t and IPC system
  - Improve thread checks to better detect broken 5.10 builds
  - Use thread checks to skip/run t/Legacy/Regression/637.t

* Mon May 23 2016 Petr Pisar <ppisar@redhat.com> - 1.302019-2
- Obsolete perl-Test2-0.000044-2 too

* Thu May 19 2016 Paul Howarth <paul@city-fan.org> - 1.302019-1
- Update to 1.302019
  - Block signals in critical IPC section (fix #661 and #668)
  - Merge Examples and examples into one dir (#660)
  - Documentation and typo fixes
  - Make Test2::Util::get_tid have a consistent prototype (#665)
  - Make TB->no_plan a no-op if a plan is set
  - Fix util.t win32 bug
  - Handle Test::Builder::Exception properly
  - Silence noisy STDERR in test suite
  - POD spelling fixes
- BR: perl-generators

* Wed May 18 2016 Paul Howarth <paul@city-fan.org> - 1.302015-1
- Update to 1.302015
  - Major refactoring of existing API on top of (included) Test2
- Obsolete/Provide perl-Test2

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.001014-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.001014-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001014-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001014-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001014-3
- Perl 5.22 rebuild

* Wed Mar 04 2015 Petr Šabata <contyk@redhat.com> - 1.001014-2
- Correct the license tag

* Wed Jan  7 2015 Paul Howarth <paul@city-fan.org> - 1.001014-1
- Update to 1.001014
  - Fix a unit test that broke on some platforms with spaces in the $^X path
  - Add a test to ensure that the Changes file is updated

* Wed Dec 24 2014 Paul Howarth <paul@city-fan.org> - 1.001012-1
- Update to 1.001012
  - Move test that was dropped in the wrong directory

* Tue Dec 23 2014 Paul Howarth <paul@city-fan.org> - 1.001011-1
- Update to 1.001011
  - Fix windows test bug (GH#491)
  - Integrate Test::Tester and Test::use::ok for easier downgrade from trial
  - Remove POD Coverage test
- Obsolete/Provide perl-Test-Tester and perl-Test-use-ok
- Classify buildreqs by usage
- Use features from recent ExtUtils::MakeMaker to simplify spec
- Run tests with AUTHOR_TESTING=1 so we do the threads test too

* Tue Nov  4 2014 Paul Howarth <paul@city-fan.org> - 1.001009-1
- Update to 1.001009
  - Backport cmp_ok fix from alphas (GH#478)

* Thu Oct 16 2014 Paul Howarth <paul@city-fan.org> - 1.001008-1
- Update to 1.001008
  - Fix subtest name when skip_all is used

* Tue Sep  9 2014 Paul Howarth <paul@city-fan.org> - 1.001006-1
- Update to 1.001006
  - Documentation updates
  - Subtests accept args
  - Outdent subtest diag
  - Changed install path for perl 5.12 or higher

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001003-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 22 2014 Paul Howarth <paul@city-fan.org> - 1.001003-1
- Update to 1.001003
  - Documentation updates for maintainer change
- This release by EXODIST -> update source URL
- Drop obsoletes/provides for old tests sub-package

* Tue Nov  5 2013 Paul Howarth <paul@city-fan.org> - 1.001002-1
- Update to 1.001002
  - Restore ability to use regex with test_err and test_out (CPAN RT#89655)
- Drop upstreamed regex patch

* Sat Oct 12 2013 Paul Howarth <paul@city-fan.org> - 0.99-1
- 0.99 bump
- This release by RJBS -> update source URL

* Fri Aug 09 2013 Petr Pisar <ppisar@redhat.com> - 0.98.05-3
- Pass regular expression intact

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 0.98.05-1
- 0.98_05 bump

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.98-244
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-243
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-242
- Update dependencies and comments

* Thu Aug 23 2012 Paul Howarth <paul@city-fan.org> - 0.98-241
- Merge tests sub-package back into main package
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Don't use macros for commands
- Mark Tutorial.pod as %%doc
- Drop explicit dependency on perl-devel

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.98-240
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 0.98-6
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.98-5
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.98-3
- Change path on vendor, so our debuginfo are not conflicting with
  perl core debuginfos

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.98-2
- Perl mass rebuild

* Thu Feb 24 2011 Iain Arnell <iarnell@gmail.com> - 0.98-1
- Update to latest upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Iain Arnell <iarnell@gmail.com> - 0.96-1
- Update to latest upstream version
- Clean up spec for modern rpmbuild

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.94-2
- Mass rebuild with perl-5.12.0

* Tue Mar 16 2010 Chris Weyl <cweyl@alumni.drew.edu> - 0.94-1
- Specfile by Fedora::App::MaintainerTools 0.006
