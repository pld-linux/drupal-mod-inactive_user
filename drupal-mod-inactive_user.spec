%define		modname inactive_user
Summary:	Drupal Inactive User Module
Summary(pl.UTF-8):	Moduł Inactive User dla Drupala
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

%description -l pl.UTF-8
Moduł inactive_user wyposaża administratorów Drupala w automatyczny
sposób zarządzania kontami nieaktywnych użytkowników. Moduł ten ma dwa
zadania: pomóc użytkownikom w powracaniu na stronę poprzez
przypominanie im, że nie byli na niej w ciągu konfigurowalnego okresu
czasu, oraz czyścić nieużywane konta.

Jedna lub więcej z następujących akcji może być podjęta dla
użytkowników, którzy przekroczyli konfigurowalny okres nieaktywności:
- wysłanie listu do użytkownika
- wysłanie listu do administratora serwisu
- zablokowanie konta (najpierw wysyłane jest ostrzeżenie, a
  powiadomienie może być wysłane do użytkownika i/lub administratora
  serwisu kiedy nastąpi zablokowanie)
- usunięcie konta (najpierw wysyłane jest ostrzeżenie, a
  powiadomienie może być wysłane do użytkownika i/lub administratora
  serwisu kiedy nastąpi usunięcie)
- opcjonalnie można zablokować usuwanie użytkowników, którzy
  stworzyli jakąś treść na stronie.

Wszystkie zdarzenia wyzwalane przez ten moduł są logowane poprzez
watchdoga.

Ten moduł nie jest już utrzymywany. Wymaga nowego maintainera.

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
