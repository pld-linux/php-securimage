# TODO
# - add web access, but secure it to keep only needed files there
%define		pkgname	securimage
%define		php_min_version 5.2.0
Summary:	PHP CAPTCHA Script
Name:		php-%{pkgname}
Version:	3.5.2
Release:	0.1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://www.phpcaptcha.org/latest.tar.gz?/%{pkgname}-%{version}.tar.gz
# Source0-md5:	5725a8ce1bb3c86e8ecedc7bc7e20a94
URL:		https://www.phpcaptcha.org/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(gd)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}

%description
Securimage is an open-source free PHP CAPTCHA script for generating
complex images and CAPTCHA codes to protect forms from spam and abuse.

It can be easily added into existing forms on your website to provide
protection from spam bots. It can run on most any webserver as long as
you have PHP installed, and GD support within PHP. Securimage does
everything from generating the CAPTCHA images to validating the typed
code. Audible codes can be streamed to the browser with Flash for the
vision impaired.

Features:
- Show an image in just 3 lines of code
- Validate submitted entries in less than 6 lines of code
- Customizable code length, character sets, and Unicode support
- TTF font support
- Easily add background images
- Several security features such as image distortion, random lines,
  and noise
- Flash button to stream audible codes in WAV format
- Ability to use a word list
- Case sensitive option for added security
- Display alphanumeric captchas, mathematical captchas, or a multi
  word captcha
- Highly customizable!

%prep
%setup -qc

mv %{pkgname}/*.{txt,ttf} .

install -d examples
mv %{pkgname}/{*.html,*example*} examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{pkgname}/* $RPM_BUILD_ROOT%{_appdir}
install -d $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt README.FONT.txt LICENSE.txt
%{php_data_dir}/securimage
%{_examplesdir}/%{name}-%{version}
