Name:           hw
Version:		0.1
Release:        1%{?dist}
Summary:

License:
URL:
Source0:

BuildRequires:
Requires:

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc

%changelog
* Fri Apr 17 2020 Mihaly Zachar <zminaly@gmail.com>
-
