#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scripttest
Version  : 1.3
Release  : 35
URL      : http://pypi.debian.net/scripttest/scripttest-1.3.tar.gz
Source0  : http://pypi.debian.net/scripttest/scripttest-1.3.tar.gz
Summary  : Helper to test command-line scripts
Group    : Development/Tools
License  : MIT
Requires: scripttest-python = %{version}-%{release}
Requires: scripttest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
scripttest
==========

.. image:: https://pypip.in/v/ScriptTest/badge.png
        :target: https://pypi.python.org/pypi/scripttest

.. image:: https://secure.travis-ci.org/pypa/scripttest.png
   :target: http://travis-ci.org/pypa/scripttest

scripttest is a library to help you test your interactive command-line
applications.

With it you can easily run the command (in a subprocess) and see the
output (stdout, stderr) and any file modifications.

* The `source repository <https://github.com/pypa/scripttest>`_.
* The `documentation <https://scripttest.readthedocs.org/>`_.

%package python
Summary: python components for the scripttest package.
Group: Default
Requires: scripttest-python3 = %{version}-%{release}

%description python
python components for the scripttest package.


%package python3
Summary: python3 components for the scripttest package.
Group: Default
Requires: python3-core
Provides: pypi(scripttest)

%description python3
python3 components for the scripttest package.


%prep
%setup -q -n scripttest-1.3
cd %{_builddir}/scripttest-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583227945
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
