Name: qm_mount_bind_ttyUSB0
Version: 0.6.8
Release: 1%{?dist}
Summary: Drop-in configuration for QM containers to mount bind ttyUSB0
License: GPL-2.0-only
URL: https://github.com/containers/qm
Source0: %{url}/archive/v%{version}.tar.gz
BuildArch: noarch

Requires: qm = %{version}-%{release}

%description
This sub-package installs drop-in configurations for QM containers to mount bind ttyUSB0.

%prep
%autosetup -Sgit -n qm-%{version}

%install
install -d %{buildroot}%{_sysconfdir}/qm/containers/containers.conf.d
install -m 644 etc/qm/containers/containers.conf.d/qm_dropin_mount_bind_ttyUSB0.conf \
    %{buildroot}%{_sysconfdir}/qm/containers/containers.conf.d/

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/qm/containers/containers.conf.d/qm_dropin_mount_bind_ttyUSB0.conf

%changelog
* Fri Jul 21 2023 RH Container Bot <rhcontainerbot@fedoraproject.org>
- Added ttyUSB0 mount bind drop-in configuration.
