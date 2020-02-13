# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate vec_map

Name:           rust-%{crate}
Version:        0.8.1
Release:        10%{?dist}
Summary:        Simple map based on a vector for small integer keys

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/vec_map
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files, https://github.com/contain-rs/vec-map/pull/41
Patch0:         vec_map-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple map based on a vector for small integer keys.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+eders-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+eders-devel %{_description}

This package contains library source intended for building other packages
which use "eders" feature of "%{crate}" crate.

%files       -n %{name}+eders-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:37:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-8
- Regenerate

* Sun Jun 09 22:11:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-7
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-6
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-4
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-3
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-3
- Rebuild for rust-packaging v5

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-2
- Exclude unneeded files

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-2
- Port to use rust-packaging

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
