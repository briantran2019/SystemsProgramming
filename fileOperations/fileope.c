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

static int filetypeletter(int mode) // reads filetype
{
    char c;

    if (S_ISREG(mode)) // regular file
        c = '-';
    else if (S_ISDIR(mode)) // directory
        c = 'd';
    else if (S_ISBLK(mode)) // block special file
        c = 'b';
    else if (S_ISCHR(mode)) // char special file
        c = 'c';
#ifdef S_ISFIFO
    else if (S_ISFIFO(mode)) // is pipe, |
        c = 'p';
#endif /* S_ISFIFO */
#ifdef S_ISLNK
    else if (S_ISLNK(mode)) // is symbolic link
        c = 'l';
#endif /* S_ISLNK */
#ifdef S_ISSOCK
    else if (S_ISSOCK(mode)) // socket
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

    bits[0] = filetypeletter(mode);         // first index stores char returned by filetype checker
    strcpy(&bits[1], rwx[(mode >> 6) & 7]); // copies
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

void details(char *filename, char file_ex, struct stat buf)
{
}

int search(char *filename, char *keyword)
{
    FILE *fp;
    int line = 1;
    int result = 0;
    char buf[512];

    if ((fp = fopen(filename, "r")) == NULL) 
    {
        printf("Error");
    }

    while(fgets(buf, 512, fp) != NULL) {
		if((strstr(buf, keyword)) != NULL) {
            result = 1;
		}
		line++;
	}
    return result;
}

int main(int argc, char *argv[])
{
    char *operation = argv[1];
    const char *file_ext = argv[2];
    char *path = argv[3];
    unsigned int num_files_found = listdir(".");
    char validFilenames[] = {0};
    struct stat buf;
    int keywordfound = 0;
    chdir(path);

    for (int i = 0; i < num_files_found; i++)
    {

        stat(filenames[i], &buf);
        if (argc == 4) 
        {
            if (strcmp(argv[1], "details") == 0)
            {
                if ((strcmp(get_filename_ext(filenames[i]), file_ext)) == 0)
                {
                    printf("Filename:     %s \n", filenames[i]);

                    int mode = buf.st_mode;
                    char *perms = lsperms(mode);
                    printf("Permissions:  %s\n", perms);

                    struct passwd *pw = getpwuid(buf.st_uid);
                    printf("Owner:        %s\n", pw->pw_name);

                    struct group *gr = getgrgid(buf.st_gid);
                    printf("group:        %s\n\n", gr->gr_name);
                }
            }
        }
        else if (argc == 5) 
        {
            if (i == 0)
            {
                printf("Keyword \"%s\" found in: ", argv[4]);
            }
            if (strcmp(argv[1], "search") == 0) 
            {
                if ((strcmp(get_filename_ext(filenames[i]), file_ext)) == 0) 
                {
                    if (search(filenames[i], argv[4]) == 1) {
                        printf("%s ", filenames[i]);
                        keywordfound = 1;
                    }
                }
            }
            if (keywordfound == 0 & i == num_files_found - 1) {
                printf("none");
            }
            if (i == num_files_found - 1)
            {
                printf("\n");
            }
        }
        else {
            printf("Usage Error - Please use 3 or 4 arguments, depending on the operation.\n");
            exit(1);
        }
    }

    /* ----------------------------------------- */
    /*
    char *fd = "hello.txt";

    //const char *file_ext = get_filename_ext(fd);
    printf("file ext: %s\n", file_ext);

    struct stat buf;
    stat(fd, &buf);
    int size = buf.st_size;
    int mode = buf.st_mode;

    char *perms = lsperms(mode);
    printf("perms: %s\n", perms);

    struct passwd *pw = getpwuid(buf.st_uid);
    printf("name: %s\n", pw->pw_name);

    struct group *gr = getgrgid(buf.st_gid);
    printf("group: %s\n\n", gr->gr_name);
    */
}