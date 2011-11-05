# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-spectra
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license lppl
# catalog-version 0.91
Name:		texlive-pst-spectra
Version:	0.91
Release:	1
Summary:	Draw continuum, emission and absorption spectra with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-spectra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-spectra.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is a PSTricks extension, based on a NASA lines
database. It allows you to draw continuum, emission and
absorption spectra. A Total of 16 880 visible lines from 99
elements can be displayed. The package requires the xkeyval
package for decoding its arguments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-spectra/pst-spectra.pro
%{_texmfdistdir}/tex/generic/pst-spectra/pst-spectra.tex
%{_texmfdistdir}/tex/latex/pst-spectra/pst-spectra.sty
%doc %{_texmfdistdir}/doc/generic/pst-spectra/README
%doc %{_texmfdistdir}/doc/generic/pst-spectra/pst-spectra.pdf
%doc %{_texmfdistdir}/doc/generic/pst-spectra/pst-spectraEN.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
