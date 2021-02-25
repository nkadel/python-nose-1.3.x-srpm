%global srcname nose
%global _description \
nose extends the test loading and running features of unittest, making\
it easier to write, find and run tests.\
\
By default, nose will run tests in files or directories under the\
current working directory whose names include "test" or "Test" at a\
word boundary (like "test_this" or "functional_test" or "TestClass"\
but not "libtest"). Test output is similar to that of unittest, but\
also includes captured stdout output from failing tests, for easy\
print-style debugging.\
\
These features, and many more, are customizable through the use of\
plugins. Plugins included with nose provide support for doctest, code\
coverage and profiling, flexible attribute-based test selection,\
output capture and more.

#Name:           python3-nose
Name:           python-nose
Version:        1.3.7
#Release:        4$%{?dist}
Release:        0%{?dist}
Summary:        Discovery-based unittest extension for Python 3

License:        LGPLv2+ and Public Domain
URL:            https://nose.readthedocs.org/en/latest/
#Source0:        %pypi_source
Source0:        http://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
# Fix python 3.5 compat
# https://github.com/nose-devs/nose/pull/983
Patch1:         python-nose-py35.patch
# Fix UnicodeDecodeError with captured output
# https://github.com/nose-devs/nose/pull/988
Patch2:         python-nose-unicode.patch
# Allow docutils to read utf-8 source
Patch3:         python-nose-readunicode.patch
# Fix Python 3.6 compatibility
# Python now returns ModuleNotFoundError instead of the previous ImportError
# https://github.com/nose-devs/nose/pull/1029
Patch4:         python-nose-py36.patch

BuildArch:      noarch
BuildRequires: dos2unix

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Discovery-based unittest extension for Python %{python3_version}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-coverage
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

This package installs the nose module and nosetests-%{python3_version} program that
can discover python%{python3_pkgversion} unittests.


%prep
%autosetup -p 1 -n %{srcname}-%{version}

dos2unix examples/attrib_plugin.py


%build
%py3_build


%install
mkdir -m 0755 -p %{buildroot}%{_mandir}/man1/

%py3_install
rm %{buildroot}%{_bindir}/nosetests
mv %{buildroot}%{_prefix}/man/man1/nosetests.1 %{buildroot}%{_mandir}/man1/nosetests-%{python3_version}.1


%check
%{__python3} setup.py build_tests
%{__python3} selftest.py -v

%files -n python%{python3_pkgversion}-%{srcname}
%license lgpl.txt
%doc AUTHORS CHANGELOG NEWS README.txt doc/*.rst doc/api doc/plugins
%{_bindir}/nosetests-%{python3_version}
%{_mandir}/man1/nosetests-%{python3_version}.1.gz
%{python3_sitelib}/nose/
%{python3_sitelib}/nose-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>
- Rebuilt to change main python from 3.4 to 3.6

* Fri Jul 13 2018 Carl George <carl@george.computer> - 1.3.7-3
- Enable python36 subpackage
- Add patches 1, 2, 3, and 4 from Fedora for py36 compatibility

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.7-2
- Fix URL
- Fix long line in description
- Include more documentation

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3.7-1
- Initial EPEL7 package
