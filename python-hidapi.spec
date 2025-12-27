%define module hidapi
%bcond tests 1

Name:		python-hidapi
Version:	0.15.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A Cython interface to the hidapi from https://github.com/libusb/hidapi
URL:		https://pypi.org/project/hidapi/
License:	 BSD-3-Clause OR GPL-3.0-or-later
Group:		Development/Python

BuildSystem:	python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(hidapi-hidraw)
BuildRequires:	pkgconfig(hidapi-libusb)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(udev)
# for tests
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pluggy)
%endif

%description
A Cython interface to the hidapi from https://github.com/libusb/hidapi

%prep
%autosetup -p1 -n %{module}-%{version}

%build
export LDFLAGS="%{optflags} -lpython%{pyver}"
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH=%{buildroot}%{python_sitearch}:%{python_sitearch}
pytest -v tests.py
%endif

%files
%license LICENSE*.txt
%doc README.rst try.py
%{python_sitearch}/hid.*.so
%{python_sitearch}/hidraw.*.so
%{python_sitearch}/%{module}-%{version}.dist-info
