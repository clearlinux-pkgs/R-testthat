#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-testthat
Version  : 3.2.2
Release  : 131
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/testthat_3.2.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/testthat_3.2.2.tar.gz
Summary  : Unit Testing for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat-lib = %{version}-%{release}
Requires: R-R6
Requires: R-brio
Requires: R-callr
Requires: R-cli
Requires: R-desc
Requires: R-digest
Requires: R-evaluate
Requires: R-jsonlite
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-pkgload
Requires: R-praise
Requires: R-processx
Requires: R-ps
Requires: R-rlang
Requires: R-waldo
Requires: R-withr
BuildRequires : R-R6
BuildRequires : R-brio
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-evaluate
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-pkgload
BuildRequires : R-praise
BuildRequires : R-processx
BuildRequires : R-ps
BuildRequires : R-rlang
BuildRequires : R-waldo
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
frustrating and boring, many of us avoid it. 'testthat' is a testing
    framework for R that is easy to learn and use, and integrates with
    your existing 'workflow'.

%package dev
Summary: dev components for the R-testthat package.
Group: Development
Requires: R-testthat-lib = %{version}-%{release}
Provides: R-testthat-devel = %{version}-%{release}
Requires: R-testthat = %{version}-%{release}

%description dev
dev components for the R-testthat package.


%package lib
Summary: lib components for the R-testthat package.
Group: Libraries

%description lib
lib components for the R-testthat package.


%prep
%setup -q -n testthat
pushd ..
cp -a testthat buildavx2
popd
pushd ..
cp -a testthat buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735113376

%install
export SOURCE_DATE_EPOCH=1735113376
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/CITATION
/usr/lib64/R/library/testthat/DESCRIPTION
/usr/lib64/R/library/testthat/INDEX
/usr/lib64/R/library/testthat/LICENSE
/usr/lib64/R/library/testthat/Meta/Rd.rds
/usr/lib64/R/library/testthat/Meta/features.rds
/usr/lib64/R/library/testthat/Meta/hsearch.rds
/usr/lib64/R/library/testthat/Meta/links.rds
/usr/lib64/R/library/testthat/Meta/nsInfo.rds
/usr/lib64/R/library/testthat/Meta/package.rds
/usr/lib64/R/library/testthat/Meta/vignette.rds
/usr/lib64/R/library/testthat/NAMESPACE
/usr/lib64/R/library/testthat/NEWS.md
/usr/lib64/R/library/testthat/R/testthat
/usr/lib64/R/library/testthat/R/testthat.rdb
/usr/lib64/R/library/testthat/R/testthat.rdx
/usr/lib64/R/library/testthat/doc/custom-expectation.R
/usr/lib64/R/library/testthat/doc/custom-expectation.Rmd
/usr/lib64/R/library/testthat/doc/custom-expectation.html
/usr/lib64/R/library/testthat/doc/index.html
/usr/lib64/R/library/testthat/doc/parallel.R
/usr/lib64/R/library/testthat/doc/parallel.Rmd
/usr/lib64/R/library/testthat/doc/parallel.html
/usr/lib64/R/library/testthat/doc/skipping.R
/usr/lib64/R/library/testthat/doc/skipping.Rmd
/usr/lib64/R/library/testthat/doc/skipping.html
/usr/lib64/R/library/testthat/doc/snapshotting.R
/usr/lib64/R/library/testthat/doc/snapshotting.Rmd
/usr/lib64/R/library/testthat/doc/snapshotting.html
/usr/lib64/R/library/testthat/doc/special-files.R
/usr/lib64/R/library/testthat/doc/special-files.Rmd
/usr/lib64/R/library/testthat/doc/special-files.html
/usr/lib64/R/library/testthat/doc/test-fixtures.R
/usr/lib64/R/library/testthat/doc/test-fixtures.Rmd
/usr/lib64/R/library/testthat/doc/test-fixtures.html
/usr/lib64/R/library/testthat/doc/third-edition.R
/usr/lib64/R/library/testthat/doc/third-edition.Rmd
/usr/lib64/R/library/testthat/doc/third-edition.html
/usr/lib64/R/library/testthat/examples/test-failure.R
/usr/lib64/R/library/testthat/examples/test-success.R
/usr/lib64/R/library/testthat/help/AnIndex
/usr/lib64/R/library/testthat/help/aliases.rds
/usr/lib64/R/library/testthat/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/testthat/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/testthat/help/figures/logo.png
/usr/lib64/R/library/testthat/help/paths.rds
/usr/lib64/R/library/testthat/help/testthat.rdb
/usr/lib64/R/library/testthat/help/testthat.rdx
/usr/lib64/R/library/testthat/html/00Index.html
/usr/lib64/R/library/testthat/html/R.css
/usr/lib64/R/library/testthat/resources/catch-routine-registration.R
/usr/lib64/R/library/testthat/resources/test-cpp.R
/usr/lib64/R/library/testthat/resources/test-example.cpp
/usr/lib64/R/library/testthat/resources/test-runner.cpp
/usr/lib64/R/library/testthat/tests/test-catch.R
/usr/lib64/R/library/testthat/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.0/snapshot-file/version.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.0/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.1/snapshot-file/version.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.1/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.2/snapshot-file/version.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.2/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.3/snapshot-file/version.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.3/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.4/snapshot-file/version.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/R4.4/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/deprec-condition.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/describe.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/edition.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-condition.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-constant.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-equality.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-inheritance.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-invisible.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-no-condition.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/expect-setequal.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/local.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/mock.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/mock2.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/quasi-label.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-check.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-debug.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-junit.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-location.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-minimal.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-progress.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-rstudio.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-silent.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-stop.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-summary.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-tap.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter-teamcity.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/reporter.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/skip.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-cleanup.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file/a.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file/foo.csv
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file/foo.png
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file/foo.r
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-file/secret.txt
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-manage.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot-value.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/source.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/test-env.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/test-files.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/test-path.md
/usr/lib64/R/library/testthat/tests/testthat/_snaps/test-state.md
/usr/lib64/R/library/testthat/tests/testthat/context.R
/usr/lib64/R/library/testthat/tests/testthat/helper-assign.R
/usr/lib64/R/library/testthat/tests/testthat/one.rds
/usr/lib64/R/library/testthat/tests/testthat/reporters/backtraces.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/context.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/error-setup.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/fail-many.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/fail.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/long-test.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/skips.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/state-change.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/successes.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/tests.R
/usr/lib64/R/library/testthat/tests/testthat/setup.R
/usr/lib64/R/library/testthat/tests/testthat/teardown.R
/usr/lib64/R/library/testthat/tests/testthat/test-bare.R
/usr/lib64/R/library/testthat/tests/testthat/test-browser.R
/usr/lib64/R/library/testthat/tests/testthat/test-capture-output.R
/usr/lib64/R/library/testthat/tests/testthat/test-catch.R
/usr/lib64/R/library/testthat/tests/testthat/test-colour.R
/usr/lib64/R/library/testthat/tests/testthat/test-compare.R
/usr/lib64/R/library/testthat/tests/testthat/test-context.R
/usr/lib64/R/library/testthat/tests/testthat/test-deprec-condition.R
/usr/lib64/R/library/testthat/tests/testthat/test-describe.R
/usr/lib64/R/library/testthat/tests/testthat/test-edition.R
/usr/lib64/R/library/testthat/tests/testthat/test-error/test-error.R
/usr/lib64/R/library/testthat/tests/testthat/test-evaluate-promise.R
/usr/lib64/R/library/testthat/tests/testthat/test-examples.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-comparison.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-condition.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-constant.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-equality.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-inheritance.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-invisible.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known-hash.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known.txt
/usr/lib64/R/library/testthat/tests/testthat/test-expect-length.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-match.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-named.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-no-condition.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-output.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-reference.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-self-test.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-setequal.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-silent.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-vector.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect_that.R
/usr/lib64/R/library/testthat/tests/testthat/test-expectation.R
/usr/lib64/R/library/testthat/tests/testthat/test-helpers.R
/usr/lib64/R/library/testthat/tests/testthat/test-label.R
/usr/lib64/R/library/testthat/tests/testthat/test-list-reporter/test-bare-expectations.R
/usr/lib64/R/library/testthat/tests/testthat/test-list-reporter/test-exception-outside-tests.R
/usr/lib64/R/library/testthat/tests/testthat/test-list-reporter/test-exercise-list-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/test-list-reporter/test-only-error.R
/usr/lib64/R/library/testthat/tests/testthat/test-local.R
/usr/lib64/R/library/testthat/tests/testthat/test-make-expectation.R
/usr/lib64/R/library/testthat/tests/testthat/test-mock.R
/usr/lib64/R/library/testthat/tests/testthat/test-mock2.R
/usr/lib64/R/library/testthat/tests/testthat/test-old-school.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel-crash.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel-outside.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel-setup.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel-startup.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel-teardown.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/tests/testthat/test-crash-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/tests/testthat/test-crash-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/crash/tests/testthat/test-crash-3.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/fail/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/fail/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/fail/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/fail/tests/testthat/test-bad.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/tests/testthat/test-ok-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/tests/testthat/test-ok-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/ok/tests/testthat/test-ok-3.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/tests/testthat/test-outside-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/tests/testthat/test-outside-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/outside/tests/testthat/test-outside-3.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/tests/testthat/setup-bad.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/tests/testthat/test-setup-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/tests/testthat/test-setup-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/setup/tests/testthat/test-setup-3.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/_snaps/snap-1.md
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/_snaps/snap-2.md
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/_snaps/snap-3.md
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/test-snap-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/test-snap-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/snap/tests/testthat/test-snap-3.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/startup/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/startup/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/startup/R/fail.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/startup/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/startup/tests/testthat/test-startup-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/teardown/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/teardown/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/teardown/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/teardown/tests/testthat/teardown-bad.R
/usr/lib64/R/library/testthat/tests/testthat/test-parallel/teardown/tests/testthat/test-teardown-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-path-present/tests/testthat/empty
/usr/lib64/R/library/testthat/tests/testthat/test-quasi-label.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-check.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-debug.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-junit.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-list.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-location.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-minimal.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-multi.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-progress.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-rstudio.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-silent.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-stop.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-summary.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-tap.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-teamcity.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-zzz.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/test-skip.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-cleanup.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-file-snaps.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-file.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-manage.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-serialize.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot-value.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot/_snaps/snapshot.md
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot/test-expect-condition.R
/usr/lib64/R/library/testthat/tests/testthat/test-snapshot/test-snapshot.R
/usr/lib64/R/library/testthat/tests/testthat/test-source.R
/usr/lib64/R/library/testthat/tests/testthat/test-source_dir.R
/usr/lib64/R/library/testthat/tests/testthat/test-srcrefs.R
/usr/lib64/R/library/testthat/tests/testthat/test-teardown.R
/usr/lib64/R/library/testthat/tests/testthat/test-teardown/test-teardown.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-env.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-example.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-files.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-path.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-state.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-that.R
/usr/lib64/R/library/testthat/tests/testthat/test-try-again.R
/usr/lib64/R/library/testthat/tests/testthat/test-verify-conditions-cr.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-conditions-lines.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-conditions.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-constructed-calls.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-output.R
/usr/lib64/R/library/testthat/tests/testthat/test-verify-output.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-unicode-false.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-unicode-true.txt
/usr/lib64/R/library/testthat/tests/testthat/test-warning/test-warning.R
/usr/lib64/R/library/testthat/tests/testthat/test-watcher.R
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/DESCRIPTION
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/NAMESPACE
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/R/config.R
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/tests/testthat/helper-config.R
/usr/lib64/R/library/testthat/tests/testthat/testConfigLoadAll/tests/testthat/test-config.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/helper_hello.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-bare-expectations.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-basic.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-empty.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-errors.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-failures.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-helper.R
/usr/lib64/R/library/testthat/tests/testthat/test_dir/test-skip.R
/usr/lib64/R/library/testthat/tests/testthat/too-many-failures.R
/usr/lib64/R/library/testthat/tests/testthat/utf8.R
/usr/lib64/R/library/testthat/tests/testthat/width-80.txt

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/include/testthat.h
/usr/lib64/R/library/testthat/include/testthat/testthat.h
/usr/lib64/R/library/testthat/include/testthat/vendor/catch.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/testthat/libs/testthat.so
/V4/usr/lib64/R/library/testthat/libs/testthat.so
/usr/lib64/R/library/testthat/libs/testthat.so
