#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * HERODOTOS
 * Herodotos is a simple logging library that allows you to log messages to your terminal
 * It is easy to use, only three functions but can make the end user experience very satisfying
*/

#ifndef __HERODOTOS_HEADER__
#define __HERODOTOS_HEADER__

// Displays an error message on the screen
// Use this when the program encounters an irrecoverable situation
void error(char *msg, FILE *stream);

// Displays a warning on screen
// Use this when simething's wrong, but there's a possible fix
void warn(char *msg, FILE *stream);

// Displays an info message on screen
// Use this to log out information of note
void info(char *msg, FILE *stream);

#endif

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"


#ifdef __HERODOTOS_IMPLEMENTATION__

void error(char *msg, FILE *stream) {
    fprintf(stream, ANSI_COLOR_RED "[ERROR] %s\n", msg);
}

void warn(char *msg, FILE *stream) {
    fprintf(stream, ANSI_COLOR_YELLOW "[WARNING] %s\n", msg);
}

void info(char *msg, FILE *stream) {
    fprintf(stream, ANSI_COLOR_CYAN "[INFO] %s\n", msg);
}

#endif