#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *getinput(char *input);

int main(int argc, char *argv[]){
long len;
char buf[BUFSIZ];
char *user_file, *pass_file;       /* Buffers for values in file */
char *  pathmem = "Members.csv";
char * pathuser = "LoggedIn.csv";
FILE * fp = fopen(pathmem, "r" );
char input[400];
int ok = 0;
char * length = getenv("CONTENT_LENGTH"); /* <- if the env var QUERY_STRING is not set... */
FILE * gp = fopen(pathuser, "a");
char *username, *password, *ignore, *temp;

printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<!DOCTYPE>");
printf("<html>");

 if (length == NULL || sscanf(length,"%ld",&len) != 1 || len > 40) {
                printf("<p>There seems to be an error </p>");
        } else {

                fgets(input,len+1,stdin);
                user_file = strtok(input, "&");
                user_file = strtok(NULL, "&");
                temp = user_file;
                username = getinput(input);
                password = getinput(temp);
                char *line = malloc(192*sizeof(char));
/* Loop through the file */
                while (fgets(line, 192, fp)) {

                        user_file = strtok(line, ",");
                        user_file = strtok(NULL, ",");

                        if(strcmp(user_file, username) == 0){
                                user_file = strtok(NULL, ",");
                                if (user_file[strlen(password)] = '\n') { user_file[strlen(password)] = '\0';        }
                                if(strcmp(password, user_file)  == 0){ ok = 1; }
                        }
                        }fclose(fp);

                        if ( ok == 0){

                        printf("<title>LOGIN</title><br>\n");
                        printf("<center>There was an error with your login!<br>");
                        printf("<a href=\"http://cs.mcgill.ca/~ysibou/\">Click here to go back to the home page!</a> <a href=\"http://cs.mcgill.ca/~ysibou/login.html\">Click here to login again!</a></center>");
                        printf("</body>");

                        } else {
		
                        fprintf(gp, "%s/n", username);
                        fclose(gp);
						printf("<title>Catalogue</title>");
        					printf("<head>");


        					printf("<body>");
        					printf("<form name=\"input\" action=\"Purchase.py\" method=\"get\">");
       						printf(" <input type=\"hidden\" name=\"username\" value=\"%s\">", username);
        					printf("<table class=\"items\" align = \"center\">");
        					printf("<tr>");
                				printf("<th> The nebula </th>");
                				printf("<th> The galaxy </th>");

       						printf(" </tr>");
        					printf("<tr>");
                				printf("<td> It's shiny</td>");
        					printf("</tr>");
						printf("<td><input type=\"checkbox\" name=\"checkneb\">Add to cart</td>");
                        			printf("<td><input type=\"checkbox\" name=\"checkgal\">Add to cart</td>");
       						printf("<tr>");
                				printf("<td> Enter purchase amount:<input type=\"positive floating-point number\" name=\"neb\" value=\"0\"></td>");
                				printf("<td> Enter purchase amount:<input type=\"number\" name=\"gal\" value=\"0\"></td>");


        					printf("</tr>");
        					printf("<tr>");
                			printf("<td><input type=\"submit\" value=\"Purchase\"></td>");
        					printf("</body>");

							printf("</html>");
                     
        

						}
}
}
/* End main() */

char *getinput(char *input) {
        char  *next;
        next = strtok(input, "=");
        next = strtok(NULL, "=");
        return next;
}
             
