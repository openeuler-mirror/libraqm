Name:				libraqm
Version:			0.7.0
Release:			3
License:			MIT
Summary:			Complex Textlayout Library
URL:				https://github.com/HOST-Oman/libraqm
Source:				https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.gz
Patch0001:          Update-text-expectation.patch

BuildRequires:      python3 freetype-devel harfbuzz-devel fribidi-devel gtk-doc gcc

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package devel
Summary:			Complex Textlayout Library
Requires:			libraqm%{?_isa} = %{version}-%{release}

%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package help
Summary:			Libraqm Documentation
BuildArch:			noarch

%description help
This package contains documentation files for raqm.

%prep
%autosetup -n raqm-%{version} -p1
sed s:python:%{__python3}:g -i tests/Makefile.in
%configure --enable-gtk-doc

%build
%make_build

%check
export LC_ALL=C.utf8
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%ldconfig_scriptlets devel

%files
%license COPYING
%{_libdir}/libraqm.so.*

%files devel
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files help
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/raqm

%changelog
* Tue Jan 11 2022 wulei <wulei80@huawei.com> - 0.7.0-3
- Fix cursor_position_GB8a.test failure

* Tue Jun 08 2021 wulei <wulei80@huawei.com> - 0.7.0-2
- fixes failed: error: no acceptable C compiler found in $PATH

* Tue Mar 2 2021 wangye <wangye70@huawei.com> - 0.7.0-1
- package init
