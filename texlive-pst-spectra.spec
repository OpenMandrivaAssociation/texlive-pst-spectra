Name:		texlive-pst-spectra
Version:	15878
Release:	2
Summary:	Draw continuum, emission and absorption spectra with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-spectra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a PSTricks extension, based on a NASA lines
database. It allows you to draw continuum, emission and
absorption spectra. A Total of 16 880 visible lines from 99
elements can be displayed. The package requires the xkeyval
package for decoding its arguments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-spectra/pst-spectra.pro
%{_texmfdistdir}/tex/generic/pst-spectra/pst-spectra.tex
%{_texmfdistdir}/tex/latex/pst-spectra/pst-spectra.sty
%doc %{_texmfdistdir}/doc/generic/pst-spectra/README
%doc %{_texmfdistdir}/doc/generic/pst-spectra/pst-spectra.pdf
%doc %{_texmfdistdir}/doc/generic/pst-spectra/pst-spectraEN.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
