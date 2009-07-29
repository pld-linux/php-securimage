Summary:	PHP CAPTCHA script for generating complex images and CAPTCHA codes
Name:		php-securimage
Version:	1.0.3.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.phpcaptcha.org/latest.tar.gz
# Source0-md5:	69752053a8ec622c78ebb1303cd83450
URL:		http://www.phpcaptcha.org/
Patch0:		paths.patch
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	php-common >= 3:4.3.0
Requires:	php-gd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
Securimage is a PHP class that is used to generate and validate
CAPTCHA images. The classes uses an existing PHP session or creates
its own if none is found to store the CAPTCHA code. Variables within
the class are used to control the style and display of the image. The
class supports TTF fonts and effects for strengthening the security of
the image. If TTF support is not available, GD fonts can be used as
well, but certain options such as transparent text and angled letters
cannot be used.

%prep
%setup -q -n securimage
%patch0 -p1

# undos the source
%{__sed} -i -e 's,\r$,,' *.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a securimage.php  $RPM_BUILD_ROOT%{php_data_dir}
cp -a gdfonts $RPM_BUILD_ROOT%{_appdir}
cp -a *.ttf $RPM_BUILD_ROOT%{_appdir}

# samples
cp -a securimage_play.php securimage_show.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example_form.php securimage_example.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a images $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%doc example_form.php securimage_example.php
%{php_data_dir}/securimage.php
%{_appdir}
%{_examplesdir}/%{name}-%{version}
