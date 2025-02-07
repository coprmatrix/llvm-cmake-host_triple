Source: https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/cmake/modules/GetHostTriple.cmake
Name: llvm-cmake-host_triple
Version: 1
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
