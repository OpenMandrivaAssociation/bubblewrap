Name:		bubblewrap
Summary:	Core execution tool for unprivileged containers
Group:		Security
Version:	0.4.1
Release:	1
License:	LGPLv2+
URL:		https://github.com/projectatomic/bubblewrap
Source0:	https://github.com/projectatomic/bubblewrap/releases/download/v%{version}/%{name}-%{version}.tar.xz

# We always run autogen.sh
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi
%configure --disable-silent-rules --with-priv-mode=none --disable-selinux

%make_build

%install
%make_install INSTALL="install -p -c"

%files
%doc COPYING
%{_datadir}/bash-completion/completions/bwrap
%{_bindir}/bwrap
%{_mandir}/man1/*
