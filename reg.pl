my $name = <<'EOF';
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
EOF

s/%files -n %{python_name}.*/${name}/g;
s/License.*/License:        BSD/g;
