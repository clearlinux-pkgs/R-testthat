#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testthat
Version  : 2.3.2
Release  : 79
URL      : https://cran.r-project.org/src/contrib/testthat_2.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/testthat_2.3.2.tar.gz
Summary  : Unit Testing for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat-lib = %{version}-%{release}
Requires: R-R6
Requires: R-cli
Requires: R-crayon
Requires: R-digest
Requires: R-ellipsis
Requires: R-evaluate
Requires: R-magrittr
Requires: R-pkgload
Requires: R-praise
Requires: R-rlang
Requires: R-withr
BuildRequires : R-R6
BuildRequires : R-cli
BuildRequires : R-crayon
BuildRequires : R-digest
BuildRequires : R-ellipsis
BuildRequires : R-evaluate
BuildRequires : R-magrittr
BuildRequires : R-pkgload
BuildRequires : R-praise
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
frustrating and boring, many of us avoid it. 'testthat' is a testing framework 
    for R that is easy to learn and use, and integrates with your existing 'workflow'.

%package lib
Summary: lib components for the R-testthat package.
Group: Libraries

%description lib
lib components for the R-testthat package.


%prep
%setup -q -c -n testthat
cd %{_builddir}/testthat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589757131

%install
export SOURCE_DATE_EPOCH=1589757131
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testthat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testthat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testthat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc testthat || :


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
/usr/lib64/R/library/testthat/examples/test-failure.R
/usr/lib64/R/library/testthat/examples/test-success.R
/usr/lib64/R/library/testthat/help/AnIndex
/usr/lib64/R/library/testthat/help/aliases.rds
/usr/lib64/R/library/testthat/help/figures/logo.png
/usr/lib64/R/library/testthat/help/paths.rds
/usr/lib64/R/library/testthat/help/testthat.rdb
/usr/lib64/R/library/testthat/help/testthat.rdx
/usr/lib64/R/library/testthat/html/00Index.html
/usr/lib64/R/library/testthat/html/R.css
/usr/lib64/R/library/testthat/include/testthat.h
/usr/lib64/R/library/testthat/include/testthat/testthat.h
/usr/lib64/R/library/testthat/include/testthat/vendor/catch.h
/usr/lib64/R/library/testthat/resources/catch-routine-registration.R
/usr/lib64/R/library/testthat/resources/test-cpp.R
/usr/lib64/R/library/testthat/resources/test-example.cpp
/usr/lib64/R/library/testthat/resources/test-runner.cpp
/usr/lib64/R/library/testthat/tests/test-catch.R
/usr/lib64/R/library/testthat/tests/testthat.R
/usr/lib64/R/library/testthat/tests/testthat/context.R
/usr/lib64/R/library/testthat/tests/testthat/helper-assign.R
/usr/lib64/R/library/testthat/tests/testthat/helper-junitmock.R
/usr/lib64/R/library/testthat/tests/testthat/helper-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/helper-testthat.R
/usr/lib64/R/library/testthat/tests/testthat/one.rds
/usr/lib64/R/library/testthat/tests/testthat/reporters/backtraces.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/check.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/debug.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/fail.R
/usr/lib64/R/library/testthat/tests/testthat/reporters/junit.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/location.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/minimal.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/progress-backtraces.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/progress.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/rstudio.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/silent.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/stop.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/summary-2.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/summary-no-dots.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/summary.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/tap.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/teamcity.txt
/usr/lib64/R/library/testthat/tests/testthat/reporters/tests.R
/usr/lib64/R/library/testthat/tests/testthat/setup.R
/usr/lib64/R/library/testthat/tests/testthat/teardown.R
/usr/lib64/R/library/testthat/tests/testthat/test-bare.R
/usr/lib64/R/library/testthat/tests/testthat/test-catch.R
/usr/lib64/R/library/testthat/tests/testthat/test-colour.R
/usr/lib64/R/library/testthat/tests/testthat/test-compare-character.R
/usr/lib64/R/library/testthat/tests/testthat/test-compare-numeric.R
/usr/lib64/R/library/testthat/tests/testthat/test-compare-time.R
/usr/lib64/R/library/testthat/tests/testthat/test-compare.R
/usr/lib64/R/library/testthat/tests/testthat/test-context.R
/usr/lib64/R/library/testthat/tests/testthat/test-cpp.R
/usr/lib64/R/library/testthat/tests/testthat/test-debug-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/test-describe.R
/usr/lib64/R/library/testthat/tests/testthat/test-environment.R
/usr/lib64/R/library/testthat/tests/testthat/test-error/test-error.R
/usr/lib64/R/library/testthat/tests/testthat/test-evaluate-promise.R
/usr/lib64/R/library/testthat/tests/testthat/test-examples.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-comparison.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-condition-custom.txt
/usr/lib64/R/library/testthat/tests/testthat/test-expect-condition.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-condition.txt
/usr/lib64/R/library/testthat/tests/testthat/test-expect-equality.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-inheritance.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-invisible.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known-hash.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known-output.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-known-value.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-length.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-logical.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-match.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-messages-warning.txt
/usr/lib64/R/library/testthat/tests/testthat/test-expect-messages.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-named.R
/usr/lib64/R/library/testthat/tests/testthat/test-expect-null.R
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
/usr/lib64/R/library/testthat/tests/testthat/test-make-expectation.R
/usr/lib64/R/library/testthat/tests/testthat/test-mock.R
/usr/lib64/R/library/testthat/tests/testthat/test-old-school.R
/usr/lib64/R/library/testthat/tests/testthat/test-path-installed/testthat-tests/testthat/empty
/usr/lib64/R/library/testthat/tests/testthat/test-path-missing/empty
/usr/lib64/R/library/testthat/tests/testthat/test-path-present/tests/testthat/empty
/usr/lib64/R/library/testthat/tests/testthat/test-quasi-label.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-junit.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-list.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-multi.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter-zzz.R
/usr/lib64/R/library/testthat/tests/testthat/test-reporter.R
/usr/lib64/R/library/testthat/tests/testthat/test-skip.R
/usr/lib64/R/library/testthat/tests/testthat/test-source.R
/usr/lib64/R/library/testthat/tests/testthat/test-source_dir.R
/usr/lib64/R/library/testthat/tests/testthat/test-teardown-1.R
/usr/lib64/R/library/testthat/tests/testthat/test-teardown-2.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-example.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-path.R
/usr/lib64/R/library/testthat/tests/testthat/test-test-that.R
/usr/lib64/R/library/testthat/tests/testthat/test-test_dir.R
/usr/lib64/R/library/testthat/tests/testthat/test-test_dir.txt
/usr/lib64/R/library/testthat/tests/testthat/test-try-again.R
/usr/lib64/R/library/testthat/tests/testthat/test-verify-conditions-lines.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-conditions.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-constructed-calls.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-output.R
/usr/lib64/R/library/testthat/tests/testthat/test-verify-output.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-unicode-false.txt
/usr/lib64/R/library/testthat/tests/testthat/test-verify-unicode-true.txt
/usr/lib64/R/library/testthat/tests/testthat/test-warning/test-warning.R
/usr/lib64/R/library/testthat/tests/testthat/test-watcher.R
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/libs/testthat.so
/usr/lib64/R/library/testthat/libs/testthat.so.avx2
/usr/lib64/R/library/testthat/libs/testthat.so.avx512
