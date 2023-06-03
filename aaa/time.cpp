
// Return the current time
//声明下面的
#include <time.h>
#include <sys/time.h>
time_t time(time_t *tloc)
{
    time_t t = 0;
    if (tloc)
        *tloc = t;
    return t;
}
int gettimeofday(struct timeval *tv, struct timezone *tz)
{
    if (tv)
    {
        tv->tv_sec = 0;
        tv->tv_usec = 0;
    }
    if (tz)
    {
        tz->tz_minuteswest = 0;
        tz->tz_dsttime = 0;
    }
    return 0;
}
int settimeofday(const struct timeval *tv, const struct timezone *tz)
{
    return 0;
}
struct tm *gmtime(const time_t *timer)
{
    return NULL;
}
struct tm *localtime(const time_t *timer)
{
    return NULL;
}
//main函数
int main()
{
    time_t t;
    time(&t);
    printf("time is %ld\n", t);
    return 0;
}