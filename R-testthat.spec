#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testthat
Version  : 0.10.0
Release  : 4
URL      : http://cran.r-project.org/src/contrib/testthat_0.10.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/testthat_0.10.0.tar.gz
Summary  : Unit Testing for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat-lib
Requires: R-crayon
Requires: R-digest
BuildRequires : R-crayon
BuildRequires : R-digest
BuildRequires : clr-R-helpers

%description
# testthat
[![Travis-CI Build Status](https://travis-ci.org/hadley/testthat.png?branch=master)](https://travis-ci.org/hadley/testthat) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/hadley/testthat?branch=master)](https://ci.appveyor.com/project/hadley/testthat)
[![Coverage Status](https://img.shields.io/coveralls/hadley/testthat.svg)](https://coveralls.io/r/hadley/testthat?branch=master)

%package lib
Summary: lib components for the R-testthat package.
Group: Libraries

%description lib
lib components for the R-testthat package.


%prep
%setup -q -c -n testthat

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library testthat
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library testthat || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/CITATION
/usr/lib64/R/library/testthat/DESCRIPTION
/usr/lib64/R/library/testthat/INDEX
/usr/lib64/R/library/testthat/LICENSE
/usr/lib64/R/library/testthat/Meta/Rd.rds
/usr/lib64/R/library/testthat/Meta/hsearch.rds
/usr/lib64/R/library/testthat/Meta/links.rds
/usr/lib64/R/library/testthat/Meta/nsInfo.rds
/usr/lib64/R/library/testthat/Meta/package.rds
/usr/lib64/R/library/testthat/NAMESPACE
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
/usr/lib64/R/library/testthat/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/libs/testthat.so
