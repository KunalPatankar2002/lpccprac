
%{
#include <stdio.h>
%}

/* Starting character sequence for multiline comment */
start \/\*

/* Ending character sequence for multiline comment */
end \*\/

/* Rule Section */
%%


\/\/.*\n


{start}.*?{end}

%%

/* Driver function */
int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s input_file\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL) {
        perror("Error opening input file");
        return 1;
    }

    FILE *output_file = fopen("output_file.c", "w");
    if (output_file == NULL) {
        perror("Error opening output file");
        fclose(input_file);
        return 1;
    }

    yyin = input_file;
    yyout = output_file;

    yylex();

    fclose(input_file);
    fclose(output_file);

    return 0;
}
