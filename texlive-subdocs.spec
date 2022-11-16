Name:		texlive-subdocs
Version:	51480
Release:	1
Summary:	Multifile documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subdocs
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdocs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subdocs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an experimental package aiming to provide a different
approach for multidocument works (mainly, books with a document
per chapter). Unlike the \include mechanism, every subdocument
is a complete normal LaTeX document and may be typeset
separately. What the package does is sharing the .aux files.
The present release is an alpha version, and no attempt has yet
been made to allow it to work with, say, hyperref.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/subdocs
%doc %{_texmfdistdir}/doc/latex/subdocs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
