#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testthat
Version  : 1.0.2
Release  : 28
URL      : http://cran.r-project.org/src/contrib/testthat_1.0.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/testthat_1.0.2.tar.gz
Summary  : Unit Testing for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat-lib
BuildRequires : clr-R-helpers

%description
# testthat
[![Travis-CI Build Status](https://travis-ci.org/hadley/testthat.svg?branch=master)](https://travis-ci.org/hadley/testthat)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/hadley/testthat?branch=master&svg=true)](https://ci.appveyor.com/project/hadley/testthat)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/testthat/master.svg)](https://codecov.io/github/hadley/testthat?branch=master)
[![CRAN version](http://www.r-pkg.org/badges/version/testthat)](https://cran.r-project.org/package=testthat)

%package lib
Summary: lib components for the R-testthat package.
Group: Libraries

%description lib
lib components for the R-testthat package.


%prep
%setup -q -c -n testthat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492799542

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492799542
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testthat
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library testthat


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
/usr/lib64/R/library/testthat/NAMESPACE
/usr/lib64/R/library/testthat/NEWS.md
/usr/lib64/R/library/testthat/R/testthat
/usr/lib64/R/library/testthat/R/testthat.rdb
/usr/lib64/R/library/testthat/R/testthat.rdx
/usr/lib64/R/library/testthat/help/AnIndex
/usr/lib64/R/library/testthat/help/aliases.rds
/usr/lib64/R/library/testthat/help/paths.rds
/usr/lib64/R/library/testthat/help/testthat.rdb
/usr/lib64/R/library/testthat/help/testthat.rdx
/usr/lib64/R/library/testthat/html/00Index.html
/usr/lib64/R/library/testthat/html/R.css
/usr/lib64/R/library/testthat/include/testthat.h
/usr/lib64/R/library/testthat/include/testthat/testthat.h
/usr/lib64/R/library/testthat/include/testthat/vendor/catch.h
/usr/lib64/R/library/testthat/libs/symbols.rds
/usr/lib64/R/library/testthat/resources/test-cpp.R
/usr/lib64/R/library/testthat/resources/test-example.cpp
/usr/lib64/R/library/testthat/resources/test-runner.cpp

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/libs/testthat.so
