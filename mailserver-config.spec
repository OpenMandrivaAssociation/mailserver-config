Name: mailserver-config
Version: 23.01
Release: 1
# For postfix
Source0: main.cf
Source1: master.cf
Source2: sqlite-virtual-aliases.cf
Source3: sqlite-virtual-domains.cf
Source4: sqlite-virtual-users.cf
Source5: sqlite-catchalls.cf
Source6: sql-virtual-aliases.cf
Source7: sql-virtual-domains.cf
Source8: sql-virtual-users.cf
Source9: sql-catchalls.cf
# For dovecot
Source100: dovecot.conf
Source101: 10-auth.conf
Source102: 10-director.conf
Source103: 10-logging.conf
Source104: 10-mail.conf
Source105: 10-master.conf
Source106: 10-ssl.conf
Source107: 15-lda.conf
Source108: 15-mailboxes.conf
Source109: 20-imap.conf
Source110: 20-lmtp.conf
Source111: 20-pop3.conf
Source112: 90-acl.conf
Source113: 90-plugin.conf
Source114: 90-quota.conf
Source115: 90-sieve.conf
Source116: 91-antispam.conf
Source117: auth-checkpassword.conf.ext
Source118: auth-deny.conf.ext
Source119: auth-dict.conf.ext
Source120: auth-ldap.conf.ext
Source121: auth-master.conf.ext
Source122: auth-passwdfile.conf.ext
Source123: auth-sql.conf.ext
Source124: auth-static.conf.ext
Source125: auth-system.conf.ext
Source126: auth-vpopmail.conf.ext
Source127: dovecot-sql.conf.ext
Source128: master.sieve
# For rspamd
Source200: rspamd-learn-spam.sh
Source201: rspamd-learn-ham.sh
Source202: rspamd-learn-spam.sieve
Source203: rspamd-learn-ham.sieve
Source204: spam-global.sieve
# For sogo
Source300: sogo.conf
Source301: sieve.creds
# Users
Source400: vmail.sysusers
# Configuration tools (command line)
Source500: mail.common
Source501: addalias
Source502: adduser
Source503: aliases
Source504: password
Source505: settings
Source506: setup
Source507: wipe
Source508: adddomain
Source509: mail.cleanup
# For nginx
Source600: nginx-sogo.conf
Source601: nginx-rspamd.conf
BuildArch: noarch
Summary: Config files for a complete mail server
URL: https://openmandriva.org/
License: GPL
Group: Servers
Requires: postfix
Requires: postfix-pgsql
Requires: dovecot
Requires: dovecot-plugins-sieve
Requires: dovecot-plugins-pgsql
Requires: rspamd
Requires: clamd
Requires: sogo
Requires: redis
Requires: cyrus-sasl
Requires: memcached
Requires: postgresql postgresql-server
Requires: nginx
Requires: opendkim
Requires: certbot
# Versioned to match known working postfix and dovecot versions
Provides: postfix-config = 3.7.3-4
Provides: dovecot-config = 2.3.20-1

%description
Config files for a complete mail server featuring SMTP,
IMAP, spam and virus checks, and more

Note: at the moment installation is not fully automated.
Do:
systemctl start redis
systemctl start clamd
systemctl start rspamd
systemctl start saslauthd
systemctl start postfix
systemctl start dovecot

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/postfix
install -c -m 644 %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} %{buildroot}%{_sysconfdir}/postfix/
mkdir -p %{buildroot}%{_sysconfdir}/dovecot/conf.d
install -c -m 644 %{S:100} %{buildroot}%{_sysconfdir}/dovecot/
install -c -m 644 %{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} %{S:107} %{S:108} %{S:109} %{S:110} %{S:111} %{S:112} %{S:113} %{S:114} %{S:115} %{S:116} %{S:117} %{S:118} %{S:119} %{S:120} %{S:121} %{S:122} %{S:123} %{S:124} %{S:125} %{S:126} %{S:127} %{buildroot}%{_sysconfdir}/dovecot/conf.d/
install -c -m 644 %{S:128} %{buildroot}%{_sysconfdir}/dovecot/
mkdir -p %{buildroot}/srv/mail/sieve/global
install -c -m 644 %{S:202} %{S:203} %{S:204} %{buildroot}/srv/mail/sieve/global/
mkdir -p %{buildroot}%{_datadir}/dovecot/sieve
install -c -m 755 %{S:200} %{S:201} %{buildroot}%{_datadir}/dovecot/sieve
mkdir -p %{buildroot}%{_sysconfdir}/sogo
install -c -m 644 %{S:300} %{S:301} %{buildroot}%{_sysconfdir}/sogo/
mkdir -p %{buildroot}%{_sysusersdir}
install -c -m 644 %{S:400} %{buildroot}%{_sysusersdir}/vmail.conf
mkdir -p %{buildroot}%{_libexecdir}/vmail
install -c -m 644 %{S:500} %{S:509} %{buildroot}%{_libexecdir}/vmail/
mkdir -p %{buildroot}%{_sbindir}
install -c -m 755 %{S:501} %{buildroot}%{_sbindir}/mail.addalias
install -c -m 755 %{S:502} %{buildroot}%{_sbindir}/mail.adduser
install -c -m 755 %{S:503} %{buildroot}%{_sbindir}/mail.aliases
install -c -m 755 %{S:504} %{buildroot}%{_sbindir}/mail.password
install -c -m 644 %{S:505} %{buildroot}%{_sysconfdir}/vmail.settings
install -c -m 755 %{S:506} %{buildroot}%{_sbindir}/mail.setup
install -c -m 755 %{S:507} %{buildroot}%{_sbindir}/mail.wipe
install -c -m 755 %{S:508} %{buildroot}%{_libexecdir}/vmail/
mkdir -p %{buildroot}%{_sysconfdir}/dovecot/sni.d
mkdir -p %{buildroot}%{_sysconfdir}/nginx/
install -c -m 644 %{S:600} %{buildroot}%{_sysconfdir}/nginx/sogo.conf
install -c -m 644 %{S:601} %{buildroot}%{_sysconfdir}/nginx/rspamd.conf

%pre
%sysusers_create_package vmail %{S:400}

%files
%{_sbindir}/*
%config %{_sysconfdir}/postfix/*.cf
%config %{_sysconfdir}/dovecot/dovecot.conf
%config %{_sysconfdir}/dovecot/conf.d/*
%{_sysconfdir}/dovecot/master.sieve
%dir %{_sysconfdir}/dovecot/sni.d
%config %{_sysconfdir}/sogo/sogo.conf
%{_sysconfdir}/sogo/sieve.creds
%config %{_sysconfdir}/vmail.settings
%config %{_sysconfdir}/nginx/sogo.conf
%config %{_sysconfdir}/nginx/rspamd.conf
%{_libexecdir}/vmail
%{_datadir}/dovecot/sieve/*.sh
%{_sysusersdir}/vmail.conf
%dir %attr(0755,vmail,vmail) /srv/mail
%dir %attr(0755,vmail,vmail) /srv/mail/sieve
%dir %attr(0755,vmail,vmail) /srv/mail/sieve/global
%attr(0644,vmail,vmail) /srv/mail/sieve/global/*.sieve
