
Name:		python-hidapi
Version:	0.14.0.post4
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/h/hidapi/hidapi-%{version}.tar.gz
Summary:	A Cython interface to the hidapi from https://github.com/libusb/hidapi
URL:		https://pypi.org/project/hidapi/
License:	GPL-3.0-or-later
Group:		Development/Python

BuildSystem:	python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(hidapi-hidraw)
BuildRequires:	pkgconfig(hidapi-libusb)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(udev)

%description
A Cython interface to the hidapi from https://github.com/libusb/hidapi

%prep
%autosetup -p1 -n hidapi-%{version}

%build
export LDFLAGS="%{optflags}"
%py_build

%install
%py3_install

%check
pytest tests.py

%files
%license LICENSE*.txt
%doc README.rst try.py
%{python_sitearch}/hid.*
%{python_sitearch}/hidraw.*
%{python_sitearch}/hidapi-%{version}.*
