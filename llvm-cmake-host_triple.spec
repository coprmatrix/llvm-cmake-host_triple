Version: 20.1.2
Source: https://raw.githubusercontent.com/llvm/llvm-project/refs/tags/llvmorg-%{version}/llvm/cmake/modules/GetHostTriple.cmake
Name: llvm-cmake-host_triple
Release: 0
License: GPLv3
Summary: Missing GetHostTriple cmake file
%description
%{summary}.

%install
install -Dm644 %{SOURCE0} "%{buildroot}/%{_libdir}/cmake/llvm/GetHostTriple.cmake"

%files
%dir %{_libdir}/cmake/llvm/
%dir %{_libdir}/cmake/
%{_libdir}/cmake/llvm/GetHostTriple.cmake
