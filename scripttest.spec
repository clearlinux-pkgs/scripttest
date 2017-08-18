#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scripttest
Version  : 1.3
Release  : 12
URL      : http://pypi.debian.net/scripttest/scripttest-1.3.tar.gz
Source0  : http://pypi.debian.net/scripttest/scripttest-1.3.tar.gz
Summary  : Helper to test command-line scripts
Group    : Development/Tools
License  : MIT
Requires: scripttest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package python
Summary: python components for the scripttest package.
Group: Default

%description python
python components for the scripttest package.


%prep
%setup -q -n scripttest-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503079745
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503079745
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
