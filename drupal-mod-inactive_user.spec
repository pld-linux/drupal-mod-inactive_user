%define		modname inactive_user
Summary:	Drupal Inactive User Module
Summary(pl):	Modu³ Inactive User dla Drupala
Name:		drupal-mod-%{modname}
Version:	0.1.cvs
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/inactive_user-cvs.tar.gz
# Source0-md5:	64a37a6264d04c51b244c58fa008b180
URL:		http://drupal.org/node/10435
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
The inactive_user module provides Drupal administrators with an
automatic way to manage inactive user accounts. This module has two
goals: to help keep users coming back to your site by reminding them
when they've been away for a configurable period of time, and to
cleanup unused accounts.

One or more of the following actions can be automatically taken for
users that have exceeded configurable periods of inactivity:
- send an email to the user
- send an email to the site administrator
- block the account (a warning can first be issued, and notification
  can be sent to the user and/or site administrator when the action
  occurs)
- delete the account (a warning can first be issued, and notification
  can be sent to the user and/or site administrator when the action
  occurs)
- optionally prevent deletion of user that have created site content

All events triggered by this module are logged via the watchdog.

This module is no longer maintained. It needs a new maintainer.

%description -l pl
Modu³ inactive_user wyposa¿a administratorów Drupala w automatyczny
sposób zarz±dzania kontami nieaktywnych u¿ytkowników. Modu³ ten ma dwa
zadania: pomóc u¿ytkownikom w powracaniu na stronê poprzez
przypominanie im, ¿e nie byli na niej w ci±gu konfigurowalnego okresu
czasu, oraz czy¶ciæ nieu¿ywane konta.

Jedna lub wiêcej z nastêpuj±cych akcji mo¿e byæ podjêta dla
u¿ytkowników, którzy przekroczyli konfigurowalny okres nieaktywno¶ci:
- wys³anie listu do u¿ytkownika
- wys³anie listu do administratora serwisu
- zablokowanie konta (najpierw wysy³ane jest ostrze¿enie, a
  powiadomienie mo¿e byæ wys³ane do u¿ytkownika i/lub administratora
  serwisu kiedy nast±pi zablokowanie)
- usuniêcie konta (najpierw wysy³ane jest ostrze¿enie, a
  powiadomienie mo¿e byæ wys³ane do u¿ytkownika i/lub administratora
  serwisu kiedy nast±pi usuniêcie)
- opcjonalnie mo¿na zablokowaæ usuwanie u¿ytkowników, którzy
  stworzyli jak±¶ tre¶æ na stronie.

Wszystkie zdarzenia wyzwalane przez ten modu³ s± logowane poprzez
watchdoga.

Ten modu³ nie jest ju¿ utrzymywany. Wymaga nowego maintainera.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To create Inactive User MySQL database tables, import:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal
EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt CHANGELOG
%doc %{modname}.mysql
%{_moddir}/*.module
