#!/usr/bin/perl 

use CGI;
my $query = CGI->new();
use warnings;


my $fullName = $query->param('inputFullName');
my $userName = $query->param('inputUserName');
my $password = $query->param('inputPassword');

open FILE , "Members.csv" or die $!;
my $control = 1;

while (my $lines = <FILE> ){

        my @data = split(',', $lines);

        if ($data[1] eq $userName){

         $control = 0;
      
                        print "Content-type: text/html\n\n";
                        print <<'eof'
                        <script language="JavaScript">
                        alert("Please pick another username!");
                        history.go(-1);
                        </script>
eof
  


        }
        
        }
        
        close FILE;


        if ($control==1){


                        open FILE, ">>Members.csv" or die $!;
                        print FILE  "$fullName,";
						print FILE "$userName,";
                        print FILE "$password\n";
						 print "Content-type: text/html\n\n";
						 print "You have registered succesfully!\n";
                print <<'eof' ;
                <HTML>

                <a href="index.html">  Click Here to go back to Home page</a>
                </HTML>
eof




                }

