#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testthat
Version  : 2.0.1
Release  : 51
URL      : https://cran.r-project.org/src/contrib/testthat_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/testthat_2.0.1.tar.gz
Summary  : Unit Testing for R
Group    : Development/Tools
License  : MIT
Requires: R-testthat-lib = %{version}-%{release}
Requires: R-evaluate
Requires: R-stringi
BuildRequires : R-evaluate
BuildRequires : R-stringi
BuildRequires : buildreq-R

%description
frustrating and boring, many of us avoid it. 'testthat' is a testing framework 
    for R that is easy learn and use, and integrates with your existing 'workflow'.

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
export SOURCE_DATE_EPOCH=1539442263

%install
export SOURCE_DATE_EPOCH=1539442263
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library testthat|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/testthat/libs/symbols.rds
/usr/lib64/R/library/testthat/resources/catch-routine-registration.R
/usr/lib64/R/library/testthat/resources/test-cpp.R
/usr/lib64/R/library/testthat/resources/test-example.cpp
/usr/lib64/R/library/testthat/resources/test-runner.cpp

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/testthat/libs/testthat.so
/usr/lib64/R/library/testthat/libs/testthat.so.avx2
/usr/lib64/R/library/testthat/libs/testthat.so.avx512
