#!/usr/bin/perl -w
#
use strict;
use warnings;

use CGI;
use DBI;

my $q = CGI->new;
my $data = $q->param('data') || '?';
my $event = $q->param('event') || '?';
my $coreid = $q->param('coreid') || '?';

print "Content-type: text/html\n\n";

my $dbh = DBI->connect("DBI:mysql:general_data",'####','##########');
unless ( $dbh ) { print "FAILED\n"; exit 2 }

$dbh->do("INSERT INTO datalog ( submissionId, coreId, param, value ) VALUES ( 999, ?, ?, ? );", undef, $coreid, 'data', $data );

print "SUCCESS\n";

$dbh->disconnect();

