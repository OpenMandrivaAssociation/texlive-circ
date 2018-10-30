# revision 15878
# category Package
# catalog-ctan /macros/generic/diagrams/circ
# catalog-date 2006-12-31 18:14:50 +0100
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-circ
Version:	1.1
Release:	12
Summary:	Macros for typesetting circuit diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/circ
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circ.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Several electrical symbols like resistor, capacitor,
transistors etc., are defined. The symbols can be connected
with wires. The package also contains an American resistor
symbol for those of us on that side of the Atlantic. The
package also has simple facilities for producing optics
diagrams; however, no-one would deny that the PSTricks pst-
optic package, or the MetaPost makecirc package does the job
better.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/circ/cibimos.mf
%{_texmfdistdir}/fonts/source/public/circ/cicirc.mf
%{_texmfdistdir}/fonts/source/public/circ/cidiod.mf
%{_texmfdistdir}/fonts/source/public/circ/cioptic.mf
%{_texmfdistdir}/fonts/source/public/circ/ciphysic.mf
%{_texmfdistdir}/fonts/source/public/circ/cirest.mf
%{_texmfdistdir}/fonts/source/public/circ/cisym.mf
%{_texmfdistdir}/fonts/source/public/circ/ciwidko.mf
%{_texmfdistdir}/fonts/source/public/circ/csym.mf
%{_texmfdistdir}/fonts/source/public/circ/defcirc.mf
%{_texmfdistdir}/fonts/tfm/public/circ/cioptic.tfm
%{_texmfdistdir}/tex/latex/circ/basic.def
%{_texmfdistdir}/tex/latex/circ/box.def
%{_texmfdistdir}/tex/latex/circ/circ.sty
%{_texmfdistdir}/tex/latex/circ/gate.def
%{_texmfdistdir}/tex/latex/circ/ic.def
%{_texmfdistdir}/tex/latex/circ/oldgate.def
%{_texmfdistdir}/tex/latex/circ/optics.def
%{_texmfdistdir}/tex/latex/circ/physics.def
%doc %{_texmfdistdir}/doc/latex/circ/COPYING
%doc %{_texmfdistdir}/doc/latex/circ/README
%doc %{_texmfdistdir}/doc/latex/circ/cidoc.tex
%doc %{_texmfdistdir}/doc/latex/circ/circ.pdf
%doc %{_texmfdistdir}/doc/latex/circ/circ.txt
%doc %{_texmfdistdir}/doc/latex/circ/cisyms.tex
%doc %{_texmfdistdir}/doc/latex/circ/index.hlp
#- source
%doc %{_texmfdistdir}/source/latex/circ/Makefile
%doc %{_texmfdistdir}/source/latex/circ/circ.drv
%doc %{_texmfdistdir}/source/latex/circ/circ.dtx
%doc %{_texmfdistdir}/source/latex/circ/circ.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 750229
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718060
- texlive-circ
- texlive-circ
- texlive-circ
- texlive-circ
- texlive-circ

