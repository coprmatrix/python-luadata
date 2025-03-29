%define pypi_name luadata
%define python_name python3-%{pypi_name}
Name:           python-%{pypi_name}
Version:        1.0.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Serialize and unserialize Python list & dictionary between Lua table

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/leafvmaple/luadata
Source:         luadata-%{version}.tar.gz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  fdupes
BuildArch:      noarch

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Serialize and unserialize Python list & dictionary between Lua table.}

%description %_description

%package -n %{python_name}
Summary:        %{summary}

%description -n %{python_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires 


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto
%if %{with test}
%check
%pyproject_check_import
%pytest
%endif

%files -n %{python_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}/__init__.py
%{python3_sitelib}/%{pypi_name}/__pycache__/*
%{python3_sitelib}/%{pypi_name}/io/__init__.py
%{python3_sitelib}/%{pypi_name}/io/__pycache__/*
%{python3_sitelib}/%{pypi_name}/io/read.py
%{python3_sitelib}/%{pypi_name}/io/write.py
%{python3_sitelib}/%{pypi_name}/serializer/__init__.py
%{python3_sitelib}/%{pypi_name}/serializer/__pycache__/*
%{python3_sitelib}/%{pypi_name}/serializer/__test__.py
%{python3_sitelib}/%{pypi_name}/serializer/serialize.py
%{python3_sitelib}/%{pypi_name}/serializer/unserialize.py

%changelog
%autochangelog

