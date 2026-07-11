%global tl_name pst-spectra
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.91
Release:	%{tl_revision}.1
Summary:	Draw continuum, emission and absorption spectra with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-spectra
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a PSTricks extension, based on a NASA lines database. It
allows you to draw continuum, emission and absorption spectra. A Total
of 16 880 visible lines from 99 elements can be displayed. The package
requires the xkeyval package for decoding its arguments.

