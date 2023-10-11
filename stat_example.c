#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <grp.h>
#include <pwd.h>
#define PATH_MAX 4096

static char filenames[PATH_MAX][PATH_MAX] = {0};

static int filetypeletter(int mode)
{
    char c;

    if (S_ISREG(mode))
        c = '-';
    else if (S_ISDIR(mode))
        c = 'd';
    else if (S_ISBLK(mode))
        c = 'b';
    else if (S_ISCHR(mode))
        c = 'c';
#ifdef S_ISFIFO
    else if (S_ISFIFO(mode))
        c = 'p';
#endif /* S_ISFIFO */
#ifdef S_ISLNK
    else if (S_ISLNK(mode))
        c = 'l';
#endif /* S_ISLNK */
#ifdef S_ISSOCK
    else if (S_ISSOCK(mode))
        c = 's';
#endif /* S_ISSOCK */
#ifdef S_ISDOOR
    /* Solaris 2.6, etc. */
    else if (S_ISDOOR(mode))
        c = 'D';
#endif /* S_ISDOOR */
    else
    {
        /* Unknown type -- possibly a regular file? */
        c = '?';
    }
    return (c);
}

/* Convert a mode field into "ls -l" type perms field. */
static char *lsperms(int mode)
{
    static const char *rwx[] = {"---", "--x", "-w-", "-wx",
                                "r--", "r-x", "rw-", "rwx"};
    static char bits[11];

    bits[0] = filetypeletter(mode);
    strcpy(&bits[1], rwx[(mode >> 6) & 7]);
    strcpy(&bits[4], rwx[(mode >> 3) & 7]);
    strcpy(&bits[7], rwx[(mode & 7)]);
    if (mode & S_ISUID)
        bits[3] = (mode & S_IXUSR) ? 's' : 'S';
    if (mode & S_ISGID)
        bits[6] = (mode & S_IXGRP) ? 's' : 'l';
    if (mode & S_ISVTX)
        bits[9] = (mode & S_IXOTH) ? 't' : 'T';
    bits[10] = '\0';
    return (bits);
}

unsigned int listdir(const char *pathname)
{
    struct dirent *dir;
    DIR *d = opendir(pathname);
    unsigned int counter = 0;
    if (d)
    {
        while ((dir = readdir(d)) != NULL)
        {
            strcpy(filenames[counter++], dir->d_name);
        }
        closedir(d);
    }

    return counter;
}

const char *get_filename_ext(const char *filename)
{
    const char *dot = strrchr(filename, '.');
    if (!dot || dot == filename)
        return "";
    return dot;
}

int main(int argc, char *argv[])
{
    char *fd = "hello.txt";

    const char *file_ext = get_filename_ext(fd);
    printf("file ext: %s\n", file_ext);

    struct stat buf;
    stat(fd, &buf);
    int size = buf.st_size;
    int mode = buf.st_mode;

    char *perms = lsperms(mode);
    printf("%s\n", perms);

    struct passwd *pw = getpwuid(buf.st_uid);
    printf("name: %s\n", pw->pw_name);

    struct group *gr = getgrgid(buf.st_gid);
    printf("group: %s\n\n", gr->gr_name);

    unsigned int num_files_found = listdir(".");
    for (int i = 0; i < num_files_found; i++)
    {
        printf("filenames: %s\n", filenames[i]);
    }
}