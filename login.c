#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){

char username[100], password[100];  
char buf[BUFSIZ];                  
char *user_file, *pass_file;       /* Buffers for values in file */
char *  pathmem = "Members.csv";
char * pathuser = "LoggedIn.csv";  
FILE * fp = fopen(pathmem, "rb");
FILE * gp = fopen(pathuser, "a");
char * input;
input = getenv("QUERY_STRING");
sscanf(input, "inputUserName=%s&inputPassword", username, password);
printf("Content-type: text/html\n\n");
printf("<html>");


  /* Loop through the file */
  while (!feof(fp)) {

      
      buf[0] = '\0';

     
      fscanf(fp, "%s", buf);

      if(strlen(buf) == 0) continue;

      user_file = buf;

      pass_file = strchr(buf, ',');

      pass_file[0] = '\0';

      pass_file++;

      if(strcmp(user_file, username) == 0){
				
        if(strcmp(password, pass_file) == 0){
						
						fprintf(gp, "%s,\n", username);
                        fclose(gp);
                        printf("<h1> You are logged in! </h1>");
          				printf("</html>");
          				
        				break;

        }else {
        
        		printf("<h1> You are not logged in</h1>");
        		printf("</html>");
        
        }

      } 

    }  
 	fclose(fp);

  }  


  /* End main() */

