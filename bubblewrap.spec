%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Name:		bubblewrap
Summary:	Core execution tool for unprivileged containers
Group:		Security
Version:	0.9.0
Release:	1
License:	LGPLv2+
URL:		https://github.com/projectatomic/bubblewrap
Source0:	https://github.com/projectatomic/bubblewrap/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	pkgconfig(libcap)
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl

%description
Bubblewrap (/usr/bin/bwrap) is a core execution engine for unprivileged
containers that works as a setuid binary on kernels without
user namespaces.

%prep
%autosetup -p1

%build
%meson \
        -Dselinux=disabled

%meson_build

%install
%meson_install

%files
%doc COPYING
%{_datadir}/bash-completion/completions/bwrap
%{_datadir}/zsh/site-functions/_bwrap
%{_bindir}/bwrap
%doc %{_mandir}/man1/*
