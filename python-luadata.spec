#
# spec file for package python-luadata
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-luadata
Version:        1.0.6
Release:        0
Summary:        Serialize and unserialize Python list & dictionary between Lua table
License:        BSD License (FIXME:No SPDX)
URL:            https://github.com/leafvmaple/luadata
Source:         luadata-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Serialize and unserialize Python list & dictionary between Lua table.

%prep
%autosetup -p1 -n luadata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check


%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/luadata
%{python_sitelib}/luadata-%{version}.dist-info

%changelog
