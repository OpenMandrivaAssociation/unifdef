# Workaround for "/usr/bin/debugedit: Cannot handle 8-byte build ID"
%define debug_package %{nil}

Name: unifdef
Version: 2.12
Release: 2
Source0: http://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz
Summary: Tool to remove ifdef statements from C/C++ code
URL: https://dotat.at/prog/unifdef/
License: BSD
Group: Development/Tools

%description
The unifdef utility selectively processes conditional C preprocessor #if
and #ifdef directives. It removes from a file both the directives and the
additional text that they delimit, while otherwise leaving the file alone.

It is useful for avoiding distractions when studying code that uses #ifdef
heavily for portability: my original motivation was to understand xterm's pty
handling code. It can be used as a lightweight preprocessor; for example the
Linux kernel uses unifdef to strip out #ifdef __KERNEL__ sections from the
headers it exports to userland. You can use unifdef with languages other than
C; for example UIT, a publisher in Cambridge uses unifdef with LaTeX.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix}
strip --strip-unneeded %{buildroot}%{_bindir}/unifdef

%files
%{_bindir}/unifdef
%{_bindir}/unifdefall
%{_mandir}/man1/unifdef.1*
%{_mandir}/man1/unifdefall.1*
