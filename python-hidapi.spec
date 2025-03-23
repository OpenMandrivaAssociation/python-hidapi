
Name:		python-hidapi
Version:	0.14.0.post4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/hidapi/hidapi-%{version}.tar.gz
Summary:	A Cython interface to the hidapi from https://github.com/libusb/hidapi
URL:		https://pypi.org/project/hidapi/
License:	None
Group:		Development/Python

BuildSystem:	python
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-cython
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(hidapi-hidraw)
BuildRequires:	pkgconfig(hidapi-libusb)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(udev)


%description
A Cython interface to the hidapi from https://github.com/libusb/hidapi

%prep
%autosetup -p1 -n hidapi-%{version}

# Remove pre-built and bundled hidapi.
#rm -rf hidapi hidapi.egg-info

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%py_build

%install
%py3_install

%files
%license LICENSE*.txt
%doc README.rst try.py
%{python_sitearch}/hid.*
%{python_sitearch}/hidraw.*
%{python_sitearch}/hidapi-%{version}.*
