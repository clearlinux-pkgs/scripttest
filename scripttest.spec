#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scripttest
Version  : 1.3
Release  : 8
URL      : https://pypi.python.org/packages/source/s/scripttest/scripttest-1.3.tar.gz
Source0  : https://pypi.python.org/packages/source/s/scripttest/scripttest-1.3.tar.gz
Summary  : Helper to test command-line scripts
Group    : Development/Tools
License  : MIT
Requires: scripttest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
scripttest
==========
.. image:: https://pypip.in/v/ScriptTest/badge.png
:target: https://pypi.python.org/pypi/scripttest

%package python
Summary: python components for the scripttest package.
Group: Default

%description python
python components for the scripttest package.


%prep
%setup -q -n scripttest-1.3

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
